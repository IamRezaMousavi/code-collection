# @Author: @IamRezaMousavi
# @Date:   2023-02-14 17:01:51
# @Last Modified by:   @IamRezaMousavi
# @Last Modified time: 2023-02-14 17:12:28
from books.models import Book
from rest_framework import generics

from .serializers import BookSerializer


class BookAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
