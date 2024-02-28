# @Author: @IamRezaMousavi
# @Date:   2023-02-14 17:20:31
# @Last Modified by:   @IamRezaMousavi
# @Last Modified time: 2023-02-14 17:24:36
from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()

    def __str__(self) -> str:
        return self.title
