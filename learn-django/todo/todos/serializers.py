# @Author: @IamRezaMousavi
# @Date:   2023-02-14 17:36:30
# @Last Modified by:   @IamRezaMousavi
# @Last Modified time: 2023-02-14 17:37:48
from rest_framework import serializers

from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'title', 'body')
