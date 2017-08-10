# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext, loader
from ..models.ratings import Rating
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

# Views for Exams

def ratings_list(request):
	ratings = Rating.objects.all()

	# try to order exams list 
	order_by = request.GET.get('order_by', '')
	if order_by in ('id', 'student', 'date_time', 'subject', 'teacher', 'mark'):
		ratings = ratings.order_by(order_by)
		if request.GET.get('reverse', '') == '1':
			ratings = ratings.reverse()
	


    		
    		


	# paginate exams
	#paginator = Paginator(ratings, 12)
	#page = request.GET.get('page')
	#try:
		#ratings = paginator.page(page)
	#except PageNotAnInteger:
		# if page not an integer, deliver first page.
		#ratings = paginator.page(1)
	#except EmptyPage:
		# if page is out of range (e.g 9999), deliver last page of results
		#ratings = paginator.page(paginator.num_pages)

	return render(request, 'students/ratings_list.html', {'ratings': ratings})

def ratings_ajax_next_page(request):
	ratings_ajax = Rating.objects.all()
	next_page = request.GET.get('next_page')
	if next_page in ('id', 'student', 'date_time', 'subject', 'teacher', 'mark'):
    		return HttpResponse(next_page)

 

def ratings_add(request):
	return HttpResponse('<h1>Mark Add Form</h1>')

def ratings_edit(request, sid):
	return HttpResponse('<h1>Edit Mark %s<h1>' % sid)

def ratings_delete(request, sid):
	return HttpResponse('<h1>Delete Mark %s</h1>' % sid)
