# -*- coding: utf-8 -*-
# @Author: @IamRezaMousavi
# @Date:   2023-02-14 16:55:27
# @Last Modified by:   @IamRezaMousavi
# @Last Modified time: 2023-02-14 16:57:59

from django.urls import path

from .views import BookListView

urlpatterns = [
    path('', BookListView.as_view(), name='home'),
]
