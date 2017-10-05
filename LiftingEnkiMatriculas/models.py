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
    student_phone = models.CharField(max_length=8) #look later for correct storing method
    student_address = models.TextField(max_length=800)
    student_guardian = models.ManytoManyField (guardian_obj)

class guardian_obj(models.Model):
    guardian_id = models.CharField(max_length=200)
    guardian_name = models.CharField(max_length=200)
    guardian_middlename = models.CharField(max_length=200)
    guardian_lastname = models.CharField(max_length=200)
    guardian_2ndlastname = models.CharField(max_length=200)
    guardian_2ndlastname = models.CharField(max_length=200)
    guardian_phone = models.CharField(max_length=8) #look later for correct storing method
    guardian_relation = models.CharField(max_length=200)

class course_obj(models.Model)
    course_name = models.CharField(max_length=200)
    course_room = models.CharField(max_length=200) #define later a room object
    course_profesor = models.ForeignKey (profesor_obj, on_delete=models.CASCADE)
    course_duration = models.DurationField()
    course_day = models.CharField(max_length=200)
    course_start = models.TimeField()
    course_seats = models.DecimalField(max_digits=5, decimal_places=5)
    course_gender = models.CharField(max_length=200)
    cours_grade = models.CharField(max_length=200)



class profesor_obj(models.Model)
    profesor_id = models.CharField(max_length=200)
    profesor_name = models.CharField(max_length=200)
    profesor_lastname = models.CharField(max_length=200)
    profesor_phone = models.CharField(max_length=8) #look later for correct storing method




