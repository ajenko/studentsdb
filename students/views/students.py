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
from ..util import paginate, get_current_group

from django.views.generic import UpdateView, DeleteView

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit 
from crispy_forms.bootstrap import FormActions
import imghdr
# Create your views here.

# Views for Students

def students_list(request):

	# check if we need to show only one group of students
	current_group = get_current_group(request)
	if current_group:
		students = Student.objects.filter(students_group=current_group)
	else:
		# otherwise show all students
		students = Student.objects.all()


	# try to order students list 
	order_by = request.GET.get('order_by', '')
	if order_by in ('id', 'last_name', 'first_name', 'ticket'):
		students = students.order_by(order_by)
		if request.GET.get('reverse', '') == '1':
			students = students.reverse()

	# apply pagination
	context = paginate(students, 10, request, {},
		var_name='students')
		
	return render(request, 'students/students_list.html', context)

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
			photo_list = ('png', 'jpeg', 'gif')
			if photo:
				if imghdr.what(photo) not in photo_list:
					errors['photo'] = u'Файли повинні мати розширення: jpeg, png, gif'
				elif len(photo) > 2097152:
					errors['photo'] = u'Розмір файла не повиннен перевищувати 2мб'
				else:
					data['photo'] = photo

			# save student
			if not errors:
				student = Student(**data)
				student.save()

				# redirect to students list 

				return HttpResponseRedirect(
					u'%s?status_message=Студента {0} {1} успішно додано!'.format(first_name, last_name) % reverse('home'))

			else:
				# render form with errors and previous user input 
				return render(request, 'students/students_add.html',
					{'groups': Group.objects.all().order_by('title'),
					'errors': errors})	

		
		elif request.POST.get('cancel_button') is not None:
			# redirect to home page on cancel button
			return HttpResponseRedirect(
				u'%s?status_message=Додавання студента скасовано!' % reverse('home'))
	else:
		#initial form render
		return render(request, 'students/students_add.html', 
		{'groups': Group.objects.all().order_by('title')})


class StudentUpdateForm(ModelForm):
	class Meta:
		model = Student
		fields = '__all__'


	def __init__(self, *args, **kwargs):
		super(StudentUpdateForm, self).__init__(*args, **kwargs)

		self.helper = FormHelper(self)

		# set form tag attributes 
		self.helper.form_action = reverse(
			'students_edit', kwargs={'pk': kwargs['instance'].id})

		self.helper.form_method = 'POST'
		self.helper.form_class = 'form-horizontal'

		# set form field properties 
		self.helper.help_text_inline = True
		self.helper.html5_required = True
		self.helper.label_class = 'col-sm-2 control-label'
		self.helper.field_class = 'col-sm-4'

		# add buttons
		self.helper.layout.append(FormActions(
			Submit('add_button', u'Зберегти', css_class = "btn btn-primary"), 
			Submit('cancel_button', u'Скасувати', css_class = "btn btn-link")
			))

class StudentUpdateView(UpdateView):
	model = Student
	template_name = 'students/students_edit.html'
	form_class = StudentUpdateForm


	def get_success_url(self):
		return u'%s?status_message=Студента успішно збережено' % reverse('home')

	def post(self, request, *args, **kwargs):
		if request.POST.get('cancel_button'):
			return HttpResponseRedirect(
				u'%s?status_message=Редагування студента відмінено' % reverse('home'))

		else:
			return super(StudentUpdateView, self).post(request, *args, **kwargs)
	


class StudentDeleteView(DeleteView):
	model = Student
	template_name = 'students/students_confirm_delete.html'

	def get_success_url(self):
		return u'%s?status_message=Студента успішно видалено!' % reverse('home')