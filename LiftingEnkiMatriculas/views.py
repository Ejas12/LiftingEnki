# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import student_obj

def student_list(request):
    student_table = student_obj.objects.order_by('student_name')
    return render(request, 'LiftingEnkiMatriculas/table_template.html', {'student_table' : student_table})