# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader	
# Create your views here.

# Views for Students

def students_list(request):
	students = (
		{'id': 1,
		 'first_name': u'Андрій',
		 'last_name': u'Кобрик',
		 'ticket': 100,
		 'image': 'img/me.jpg'},
		{'id': 2,
		 'first_name': u'Міла',
		 'last_name': u'Спілберг',
		 'ticket': 101,
		 'image': 'img/1.jpeg'},
		{'id': 3,
		 'first_name': u'Арнольд',
		 'last_name': u'Шварц',
		 'ticket': 102,
		 'image': 'img/2.jpeg'},
		)
	return render(request, 'students/students_list.html', {'students': students})

def students_add(request):
	return HttpResponse('<h1>Students Add Form</h1>')

def students_edit(request, sid):
	return HttpResponse('<h1>Edit Student %s<h1>' % sid)

def students_delete(request, sid):
	return HttpResponse('<h1>Delete Student %s</h1>' % sid)
