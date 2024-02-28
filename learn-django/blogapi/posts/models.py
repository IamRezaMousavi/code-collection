# @Author: @IamRezaMousavi
# @Date:   2023-02-14 19:05:18
# @Last Modified by:   @IamRezaMousavi
# @Last Modified time: 2023-02-14 19:10:09
from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
