# -*- coding: utf-8 -*-
# @Author: @IamRezaMousavi
# @Date:   2023-02-10 16:51:21
# @Last Modified by:   @IamRezaMousavi
# @Last Modified time: 2023-02-14 16:30:58
from django.contrib import admin

from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1

class QuestionAdmin(admin.ModelAdmin):
    field = ['pub_date', 'question_text']
    list_display = ['question_text', 'pub_date', 'was_published_recently']
    inlines = [ChoiceInline]

    list_filter = ['pub_date']
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)
