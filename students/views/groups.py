# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader	
from ..models.groups import Group
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

# Views for Groups
def groups_list(request):
	groups = Group.objects.all()


	# try to order groups list 
	order_by = request.GET.get('order_by', '')
	if order_by in ('id', 'title', 'leader'):
		groups = groups.order_by(order_by)
		if request.GET.get('reverse', '') == '1':
			groups = groups.reverse()


	# paginate groups
	paginator = Paginator(groups, 4)
	page = request.GET.get('page')
	try:
		groups = paginator.page(page)
	except PageNotAnInteger:
		# if page not an integer, deliver first page.
		groups = paginator.page(1)
	except EmptyPage:
		# if page is out of range (e.g 9999), deliver last page of results
		groups = paginator.page(paginator.num_pages)
	
	return render(request, 'students/groups_list.html', {'groups': groups})

def groups_add(request):
	return HttpResponse('<h1>Group Add Form</h1>')

def groups_edit(request, gid):
	return HttpResponse('<h1>Edit Group %s</h1>' % gid)

def groups_delete(request, gid):
	return HttpResponse('<h1>Delete Group %s</h1>' % gid)


	

