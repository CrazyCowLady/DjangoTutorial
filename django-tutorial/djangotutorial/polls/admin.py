from django.contrib import admin

from .models import Question, Choice

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Question Details", {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"]}),
    ]

class ChoiceAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Related Question", {"fields": ["question"]}),
        ("Choice", {"fields": ["choice_text"]}),
        (None, {"fields": ["votes"]}),
    ]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)