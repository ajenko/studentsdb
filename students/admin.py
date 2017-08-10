# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from models.students import Student
from models.groups import Group
from models.exams import Exam
from models.ratings import Rating


# Register your models here.

admin.site.register(Student)
admin.site.register(Group)
admin.site.register(Exam)
admin.site.register(Rating)
