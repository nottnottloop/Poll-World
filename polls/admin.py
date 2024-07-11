from django.contrib import admin

from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    list_display = ["question_text", "pub_date", "was_published_recently", "last_activity"]
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date", "last_activity"]}),
    ]
    inlines = [ChoiceInline]
    list_filter = ["pub_date", "last_activity"]
    search_fields = ["question_text"]


admin.site.register(Question, QuestionAdmin)
