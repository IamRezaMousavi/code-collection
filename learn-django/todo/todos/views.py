# @Author: @IamRezaMousavi
# @Date:   2023-02-14 17:20:31
# @Last Modified by:   @IamRezaMousavi
# @Last Modified time: 2023-02-14 17:40:14
from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import Todo
from .serializers import TodoSerializer


class ListTodo(ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class DetailTodo(RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
