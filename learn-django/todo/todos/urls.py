# -*- coding: utf-8 -*-
# @Author: @IamRezaMousavi
# @Date:   2023-02-14 17:33:20
# @Last Modified by:   @IamRezaMousavi
# @Last Modified time: 2023-02-14 17:35:54
from django.urls import path

from .views import ListTodo, DetailTodo

urlpatterns = [
    path('<int:pk>/', DetailTodo.as_view()),
    path('', ListTodo.as_view()),
]
