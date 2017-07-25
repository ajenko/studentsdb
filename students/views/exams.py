# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader	
from ..models import Exam
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

# Views for Exams

def exams_list(request):
	exams = Exam.objects.all()

	# paginate exams
	paginator = Paginator(exams, 3)
	page = request.GET.get('page')
	try:
		exams = paginator.page(page)
	except PageNotAnInteger:
		# if page not an integer, deliver first page.
		exams = paginator.page(1)
	except EmptyPage:
		# if page is out of range (e.g 9999), deliver last page of results
		exams = paginator.page(paginator.num_pages)
	return render(request, 'students/exams_list.html', {'exams': exams})

def exams_add(request):
	return HttpResponse('<h1>Exam Add Form</h1>')

def exams_edit(request, sid):
	return HttpResponse('<h1>Edit Exam %s<h1>' % pid)

def exams_delete(request, sid):
	return HttpResponse('<h1>Delete Exam %s</h1>' % pid)
