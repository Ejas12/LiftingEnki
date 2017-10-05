# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class student_obj(models.Model):
    student_id = models.CharField(max_length=200)
    student_name = models.CharField(max_length=200)
    student_middlename = models.CharField(max_length=200)
    student_lastname = models.CharField(max_length=200)
    student_2ndlastname = models.CharField(max_length=200)
    student_2ndlastname = models.CharField(max_length=200)
    student_birthday = models.DateTimeField('Cumpleanos')
    student_grade = models.CharField(max_length=200)
    student_gender = models.CharField(max_length=200)
    student_phone = models.CharField(max_length=8)
    student_address = models.TextField(max_length=800)
    studen_guardian = models.ManytoManyField (guardian_obj)

class guardian_obj(models.Model):
    guardian1_id = models.CharField(max_length=200)
    guardian1_name = models.CharField(max_length=200)
    guardian1_middlename = models.CharField(max_length=200)
    guardian1_lastname = models.CharField(max_length=200)
    guardian1_2ndlastname = models.CharField(max_length=200)
    guardian1_2ndlastname = models.CharField(max_length=200)
    guardian1_phone = models.CharField(max_length=8)
    guardian1_relation = models.CharField(max_length=200)