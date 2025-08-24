# @Author: @IamRezaMousavi
# @Date:   2023-02-14 16:45:49
# @Last Modified by:   @IamRezaMousavi
# @Last Modified time: 2023-02-14 16:48:40
from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=20)
    subtitle = models.CharField(max_length=250)
    author = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.title
