# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import student_obj
from .models import profesor_obj
from .models import course_obj
from .models import guardian_obj

admin.site.register(student_obj)
admin.site.register(profesor_obj)
admin.site.register(guardian_obj)
admin.site.register(course_obj)