# @Author: @IamRezaMousavi
# @Date:   2023-02-14 19:21:34
# @Last Modified by:   @IamRezaMousavi
# @Last Modified time: 2023-02-14 19:23:15
from django.urls import path

from .views import PostDetail, PostList

urlpatterns = [path('<int:pk>/', PostDetail.as_view()), path('', PostList.as_view())]
