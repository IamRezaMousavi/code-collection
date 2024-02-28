# @Author: @IamRezaMousavi
# @Date:   2023-02-14 19:23:33
# @Last Modified by:   @IamRezaMousavi
# @Last Modified time: 2023-02-14 19:25:18
from rest_framework import serializers

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'author', 'title', 'body', 'created_at')
