# @Author: @IamRezaMousavi
# @Date:   2023-02-14 17:03:26
# @Last Modified by:   @IamRezaMousavi
# @Last Modified time: 2023-02-14 17:05:13
from django.urls import path

from .views import BookAPIView

urlpatterns = [
    path('', BookAPIView.as_view()),
]
