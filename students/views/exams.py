from __future__ import unicode_literals
from django.utils.translation import ugettext as _

from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader	
from ..models.exams import Exam
from ..models.groups import Group
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from ..util import paginate, get_current_group 
from datetime import datetime
from django.forms import ModelForm

from django.views.generic import UpdateView, DeleteView

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.bootstrap import FormActions
# Create your views here.

# Views for Exams

def exams_list(request):
	# check if we need to show only one group in exams
	current_group = get_current_group(request)
	if current_group:
		exams = Exam.objects.filter(group=current_group)
	else:
		# otherwise show all exams
		exams = Exam.objects.all()

	# try to order exams list 
	order_by = request.GET.get('order_by', '')
	if order_by in ('id', 'subject', 'teacher', 'date_time', 'group'):
		exams = exams.order_by(order_by)
		if request.GET.get('reverse', '') == '1':
			exams = exams.reverse()

	# apply pagination
	context = paginate(exams, 12, request, {},
		var_name='exams')

	
	return render(request, 'students/exams_list.html', context)

def exams_add(request):

	# IT DOESN`T WORK NOW!!!
	#  was form posted?
	if request.method == "POST":
		# was form add button clicked?
		if request.POST.get('add_button') is not None:
			# errors collection
			errors = {}

			# validate exam data will go here
			data = {'notes': request.POST.get('notes')}

			# validate user input 
			subject = request.POST.get('subject', '').strip()
			if not subject:
				errors['subject'] = _(u"Subject field is required")
			else:
				data['subject'] = subject
		
			date_time = request.POST.get('date_time', '').strip()
			if not date_time:
				errors['date_time'] = u"Date and time field is required"
			else:
				try:
					datetime.strptime(date_time, '%Y-%m-%d %H:%M:%S')
				except Exception:
					errors['date_time'] = u'Enter the correct input format(2017-09-01 12:00:00'
				else:
					data['date_time'] = date_time	
		
			teacher = request.POST.get('teacher', '').strip()
			if not teacher:
				errors['teacher'] = _(u"Teacher filed is required")
			else:
				data['teacher'] = teacher

			group = request.POST.get('group', '').strip()
			if not group:
				errors['group'] = _(u"Choose a students group")
			else:
				groups = Group.objects.filter(pk=group)
				if len(groups) != 1:
					errors['group'] = _(u"Choose a correct students group")
				else:	
					data['group'] = groups[0]

			# save exam
			if not errors:
				exam = Exam(**data)
				exam.save()

				#redirect to exams list
				return HttpResponseRedirect(
					u'%s?status_message=%s' % (reverse('exams'), _(u'The exam {0} added successfully!').format(subject)))

			else:
				# render form with errors and previous user input
				return render(request, 'students/exams_add.html',
					{'groups': Group.objects.all().order_by('title'),
					'errors': errors})

		elif request.POST.get('cancel_button') is not None:
			# redirect to home page on cancel button
			return HttpResponseRedirect(
				u'%s?status_message=%s' % (reverse('exams'), _(u'The exam add is canceled!')))
	else:
		# initial form render
		return render(request, 'students/exams_add.html',
			{'groups': Group.objects.all().order_by('title')})

class ExamUpdateForm(ModelForm):
	class Meta:
		model = Exam
		fields = '__all__'

	def __init__(self, *args, **kwargs):
		super(ExamUpdateForm, self).__init__(*args, **kwargs)

		self.helper = FormHelper(self)
		# set form tag attributes
		self.helper.form_action = reverse(
			'exams_edit', kwargs={'pk': kwargs['instance'].id})

		self.helper.form_method = 'POST' 
		self.helper.form_class = 'form-horizontal'

		# set form field properties
		self.helper.help_text_inline = True
		self.helper.html5_required = True
		self.helper.label_class = 'col-sm-2 control-label'
		self.helper.field_class = 'col-sm-4'

		# add buttons
		self.helper.layout.append(FormActions(
			Submit('add_button', _(u'Save'), css_class="btn btn-primary"), 
			Submit('cancel_button', _(u'Cancel'), css_class="btn btn-link")))


class ExamUpdateView(UpdateView):
	model = Exam
	template_name = 'students/exams_edit.html'
	form_class = ExamUpdateForm

	def get_success_url(self):
		return u'%s?status_message=%s' % (reverse('exams'), _(u'The exam updated successfully!'))
	
	def post(self, request, *args, **kwargs):
		if request.POST.get('cancel_button'):
			return HttpResponseRedirect(
				u'%s?status_message=%s' % (reverse('exams'), _(u'The exam update is canceled!')))
		else:
			return super(ExamUpdateView, self).post(request, *args, **kwargs)

class ExamDeleteView(DeleteView):
	model = Exam
	template_name = 'students/exams_confirm_delete.html'

	def get_success_url(self):
		return u'%s?status_message=%s' % (reverse('exams'), _(u'The exam deleted successfully!'))

