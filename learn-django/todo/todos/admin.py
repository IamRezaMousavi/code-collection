# -*- coding: utf-8 -*-
# @Author: @IamRezaMousavi
# @Date:   2023-02-14 17:20:31
# @Last Modified by:   @IamRezaMousavi
# @Last Modified time: 2023-02-14 17:26:03
from django.contrib import admin

from .models import Todo

admin.site.register(Todo)
