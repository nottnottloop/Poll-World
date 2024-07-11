from django.db.models import F
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