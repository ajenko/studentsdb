# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader	
# Create your views here.

# Views for Journal 

def journal_dt(request):
	journal = (
		{"id": 1,
		 "student": {"id": 1, "name": u"Кобрик Андрій"}},
		{"id": 2,
		 "student": {"id": 2, "name": u"Спілберг Міла"}},
		{"id": 3,
		 "student": {"id": 3, "name": u"Шварц Арнольд"}},
		)
	return render(request, 'students/journal.html', {"journal": journal})

