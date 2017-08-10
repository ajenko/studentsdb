# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.core.urlresolvers import reverse 
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader	
from ..models.students import Student
from ..models.groups import Group
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.forms import ModelForm, DateField
from studentsdb import settings
from datetime import datetime
# Create your views here.

# Views for Students

def students_list(request):
	students = Student.objects.all()


	# try to order students list 
	order_by = request.GET.get('order_by', '')
	if order_by in ('id', 'last_name', 'first_name', 'ticket'):
		students = students.order_by(order_by)
		if request.GET.get('reverse', '') == '1':
			students = students.reverse()

	# paginate students
	paginator = Paginator(students, 12)
	page = request.GET.get('page')
	try:
		students = paginator.page(page)
	except PageNotAnInteger:
		# if page not an integer, deliver first page.
		students = paginator.page(1)
	except EmptyPage:
		# if page is out of range (e.g 9999), deliver last page of results
		students = paginator.page(paginator.num_pages)


		#page = request.GET.get('page', '')
		
	return render(request, 'students/students_list.html', {'students': students})

def students_add(request):
	
	# was form posted?
	if request.method == "POST":
		# was form add button clicked?
		if request.POST.get('add_button') is not None:
			
			# errors collection 
			errors = {}

			# validate student data will go here
			data = {'middle_name': request.POST.get('middle_name'),
					'notes': request.POST.get('notes')}
			
			# validate user input 
			first_name = request.POST.get('first_name', '').strip()
			if not first_name:
				errors['first_name'] = u"Ім'я є обов'язковим"
			else:
				data['first_name'] = first_name 

			last_name = request.POST.get('last_name', '').strip()
			if not last_name:
				errors['last_name'] = u"Прізвище є обов'язковим"
			else:
				data['last_name'] = last_name

			birthday = request.POST.get('birthday', '').strip()
			if not birthday:
				errors['birthday'] = u"Дата народження є обов'язковою"
			else:
				try:
					datetime.strptime(birthday, '%Y-%m-%d')
				except Exception:
					errors['birthday'] = u'Введіть коректний формат дати (напр. 1990-12-31)'
				else:
					data['birthday'] = birthday

			ticket = request.POST.get('ticket', '').strip()
			if not ticket:
				errors['ticket'] = u"Номер білета є обов'язковим"
			else:
				data['ticket'] = ticket

			students_group = request.POST.get('students_group', '').strip()
			if not students_group:
				errors['students_group'] = u"Оберіть групу для студента"
			else:
				groups = Group.objects.filter(pk=students_group)
				if len(groups) != 1:
					errors['students_group'] = u"Оберіть коректну групу"
				else:	
					data['students_group'] = groups[0]

			photo = request.FILES.get('photo')
			if photo:
				data['photo'] = photo

			# save student
			if not errors:
				student = Student(**data)
				student.save()

				# redirect to students list 

				return HttpResponseRedirect(u'%s?status_message=Студента успішно додано!' % reverse('home'))

			else:
				# render from with errors and previous user input 
				return render(request, 'students/students_add.html',
					{'groups': Group.objects.all().order_by('title'),
					'errors': errors})	

		
		elif request.POST.get('cancel_button') is not None:
			# redirect to home page on cancel button
			return HttpResponseRedirect(u'%s?status_message=Додавання студента скасовано!' % reverse('home'))
	else:
		#initial form render
		return render(request, 'students/students_add.html', 
		{'groups': Group.objects.all().order_by('title')})

		

def students_edit(request, sid):
	return HttpResponse('<h1>Edit Student %s<h1>' % sid)

def students_delete(request, sid):
	return HttpResponse('<h1>Delete Student %s</h1>' % sid)
