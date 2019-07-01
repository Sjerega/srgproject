from django.contrib import admin
from polls.models import Question, Choice


class QuestionAdmin(admin.ModelAdmin):
    list_display = ["question_text", "pub_date", ]


class ChoiceAdmin(admin.ModelAdmin):
    pass


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
