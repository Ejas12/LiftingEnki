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

def login_page(request):
    return render(request, 'LiftingEnkiMatriculas/login.html')

def main_menu (request):
    return render(request, 'LiftingEnkiMatriculas/mainmenu.html')
def student_detail (request):
    student_selected = student_obj.objects.filter(student_id = student_id_selected)
    return render request 'LiftingEnkiMatriculas/studentdetails.html'

#def student_view_details (request):
 #   student_details = student_obj.objects.all() # make view to filter by user.

