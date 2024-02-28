# -*- coding: utf-8 -*-
# @Author: @IamRezaMousavi
# @Date:   2023-02-14 19:05:18
# @Last Modified by:   @IamRezaMousavi
# @Last Modified time: 2023-02-14 19:13:29
from django.contrib import admin

from .models import Post

admin.site.register(Post)
