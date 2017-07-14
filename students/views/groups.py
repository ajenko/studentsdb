# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader	
# Create your views here.

# Views for Groups
def groups_list(request):
	groups = (
		{'id': 1,
		 'name': u'МтМ-21', 
		 'leader': {'id': 1, 'name': u'Ячменев Олег'}},
		{'id': 2,
		 'name': u'МтМ-22', 
		 'leader': {'id': 2, 'name': u'Іванов Андрій'}},
		{'id': 3,
		 'name': u'МтМ-23', 
		 'leader': {'id': 3, 'name': u'Подоба Віталій'}},
		)
	return render(request, 'students/groups_list.html', {'groups': groups})

def groups_add(request):
	return HttpResponse('<h1>Group Add Form</h1>')

def groups_edit(request, gid):
	return HttpResponse('<h1>Edit Group %s</h1>' % gid)

def groups_delete(request, gid):
	return HttpResponse('<h1>Delete Group %s</h1>' % gid)


	

