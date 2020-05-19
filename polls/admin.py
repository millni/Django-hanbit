# from django.contrib import admin

# Register your models here.
from django.contrib import admin
from polls.models import Question, Choice

class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']  # 필드 순서 변경

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
