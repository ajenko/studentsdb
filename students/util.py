# -*- coding: utf-8 -*-
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from django.conf import settings
from django.utils.translation import LANGUAGE_SESSION_KEY
from studentsdb.settings import LANGUAGE_CODE


def paginate(objects, size, request, context, var_name = 'object_list'):

	""" Paginate objects provided by view

	This function takesL
		* list of elements;
		* number of objects per page;
		* request object to get url parameters from;
		* context to set new variables into;
		* var_name - variable name for list of objects.

	It returns updated context object. """

	# apply pagination 
	paginator = Paginator(objects, size)
	
	# try to get page number from request 

	page = request.GET.get('page', '1')
	try:
		object_list = paginator.page(page)
	except PageNotAnInteger:
		# if page is not an integer, deliver first page
		object_list = paginator.page(1)
	except EmptyPage:
		# if page is out of range (e.g. 9999),
		# deliver last page of result
		object_list = paginator.page(paginator.num_pages)

	# set variables into context
	context[var_name] = object_list
	context['is_paginated'] = object_list.has_other_pages()
	context['page_obj'] = object_list
	context['paginator'] = paginator

	return context

def get_groups(request):
	""" Returns list of existing groups"""
	# deferred import of Group model to avoid cycled imports
	from .models.groups import Group

	# get currently selected group 
	cur_group = get_current_group(request)

	groups = []
	for group in Group.objects.all().order_by('title'):
		groups.append({
			'id': group.id,
			'title': group.title,
			'leader': group.leader and (u'%s %s' % (group.leader.first_name, group.leader.last_name)) or None,
			'selected': cur_group and cur_group.id == group.id and True or False 
			})
		
	return groups

def get_current_group(request):
	""" Returns a currently selected group or None """ 
	# we remember a selected group in a cookie
	pk = request.COOKIES.get('current_group')
	if pk:
		from .models.groups import Group
		try:
			group = Group.objects.get(pk=int(pk))
		except Group.DoesNotExist:
			return None
		else:
			return group
	else:
		return None

def choose_lang(request):
	if request.session[LANGUAGE_SESSION_KEY] == 'uk':
		lg = u'Українська'
		return lg
	elif request.session[LANGUAGE_SESSION_KEY] == 'en':
		lg = u'English'
	else:
		if LANGUAGE_CODE == 'uk':
			lg = u'Українська'
		elif LANGUAGE_CODE == 'en':
			lg = u'English'
		else:
			lg = u'Select'
		return lg 


'''
def choose_lang(request):
	""" Choose current app language """
	lang = request.COOKIES.get(settings.LANGUAGE_COOKIE_NAME, 'uk-UK')
	print 'Lang is:' + str(lang)
	print 'lang is:' + str(settings.LANGUAGE_COOKIE_NAME)
	response_dict = {'django_lang': ''}

	if lang: 
		import logging
		try:
			response_dict['django_lang'] = settings.LANGUAGE_COOKIE_NAME
		except Exception as e:
			logger = logging.getLogger(__name__)
			logger.exception('Error during setting language. Was tried {0} language'.format(lang))
		else:
			logger = logging.getLogger(__name__)
			logger.info('Was set {0} language.'.format(lang))

	return JsonResponse(response_dict, safe=False)
	''' 