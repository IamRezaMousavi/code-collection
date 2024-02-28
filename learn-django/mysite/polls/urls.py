# -*- coding: utf-8 -*-
# @Author: @IamRezaMousavi
# @Date:   2023-02-10 17:55:56
# @Last Modified by:   @IamRezaMousavi
# @Last Modified time: 2023-02-10 22:28:19
from django.urls import path

from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/resualt/', views.ResualtView.as_view(), name='resualt'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
