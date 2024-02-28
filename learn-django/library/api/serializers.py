# -*- coding: utf-8 -*-
# @Author: @IamRezaMousavi
# @Date:   2023-02-14 17:10:19
# @Last Modified by:   @IamRezaMousavi
# @Last Modified time: 2023-02-14 17:12:04
from rest_framework import serializers

from books.models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title', 'subtitle', 'author')
