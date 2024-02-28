# @Author: @IamRezaMousavi
# @Date:   2023-02-14 16:45:49
# @Last Modified by:   @IamRezaMousavi
# @Last Modified time: 2023-02-14 16:55:02
from django.views.generic import ListView

from .models import Book


class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'
