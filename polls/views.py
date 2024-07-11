from typing import Any
from django.db.models import F, Sum
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Choice, Question


class IndexView(generic.ListView):
    template_name = "polls/pages/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        return Question.objects.all().order_by("-last_activity")


class AboutView(generic.TemplateView):
    template_name = "polls/pages/about.html"

class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/pages/vote.html"
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/pages/results.html"

class ResultsInfoView(generic.DetailView):
    model = Question

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        colors = ["blue", "green", "orange", "cornflowerblue", "red", "violet"]
        choices = context['question'].choice_set.all()
        total_votes = choices.aggregate(Sum("votes", default=0))['votes__sum']
        choices = context['question'].choice_set.all().values()
        context['choices'] = choices
        pie_information = []
        accumulator = 0
        for i in range(len(choices)):
            context['choices'][i]['color'] = colors[i]
            percent = (choices[i]['votes'] / total_votes) * 100
            pie_information.append({"color": colors[i], "dasharray_value": percent, "dashoffset_value": accumulator})
            accumulator += percent
        context['pie_information'] = pie_information
        return context

    template_name = "polls/snippets/results_info.html"

class ThanksView(generic.TemplateView):
    template_name = "polls/snippets/thanks_for_voting.html"

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/snippets/vote_form.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        question.last_activity = timezone.now()
        question.save()
        return render(request, "polls/snippets/thanks_for_voting.html", {"question": question})