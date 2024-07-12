from django import forms
from django_select2 import forms as s2forms

from . import models


class QuestionWidget(s2forms.ModelSelect2Widget):
    search_fields = [
        "question_text",
    ]


class ChoiceWidget(s2forms.ModelSelect2MultipleWidget):
    search_fields = [
        "choice_text",
    ]


class QuestionForm(forms.ModelForm):
    class Meta:
        model = models.Question
        fields = "__all__"
        widgets = {
            "question": QuestionWidget,
        }