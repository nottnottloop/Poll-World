from django import forms
from django_select2 import forms as s2forms

from . import models


class QuestionWidget(s2forms.ModelSelect2Widget):
    model = models.Question
    search_fields = [
        "question_text__icontains",
    ]

class QuestionForm(forms.ModelForm):
    class Meta:
        model = models.Question
        fields = ('question_text',)
        attrs = {
            "data-minimum-input-length": 0
        }
        widgets = {
            "question_text": QuestionWidget(attrs),
        }