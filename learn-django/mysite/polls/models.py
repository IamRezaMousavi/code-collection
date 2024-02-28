# -*- coding: utf-8 -*-
# @Author: @IamRezaMousavi
# @Date:   2023-02-10 16:51:21
# @Last Modified by:   @IamRezaMousavi
# @Last Modified time: 2023-02-14 16:28:52
import datetime

from django.db import models
from django.contrib import admin
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('Date Published')

    def __str__(self) -> str:
        return self.question_text
    
    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?'
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.choice_text
