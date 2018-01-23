from __future__ import unicode_literals
from django.utils.translation import ugettext as _

from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext, loader
from ..models.ratings import Rating
from ..models.students import Student
from django.forms import ModelForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from ..util import paginate
from datetime import datetime

from django.views.generic import UpdateView, DeleteView

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.bootstrap import FormActions

from django.contrib.auth.decorators import login_required
from .dispatch_view import Dispatch
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

	context = paginate(ratings, 10, request, {}, var_name='ratings')
	return render(request, 'students/ratings_list.html', context)
    		

"""
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

 """
@login_required
def ratings_add(request):
	# was form posted?
	if request.method == "POST":
		# was form add button clicked?
		if request.POST.get('add_button') is not None:
			# errors collection
			errors = {}

			# validate ratings data
			data = {'notes': request.POST.get('notes')}

			# validate user input
			student = request.POST.get('student', '').strip()
			if not student:
				errors['student'] = _(u'Choose the student')
			else:
				students = Student.objects.filter(pk=student)
				if len(students) != 1:
					errors['student'] = _(u'Choose a correct student')
				else:
					data['student'] = students[0]

			date_time = request.POST.get('date_time', '').strip()
			if not date_time:
				errors['date_time'] = _(u"Date and time field is required")
			else:
				try:
					datetime.strptime(date_time, '%Y-%m-%d %H:%M:%S')
				except Exception:
					errors['date_time'] = _(u"Enter a correct input format (2017-09-01 12:00:00)")
				else: 
					data['date_time'] = date_time

			subject = request.POST.get('subject', '').strip()
			if not subject:
				errors['subject'] = _(u'Subject field is required')
			else:
				data['subject'] = subject

			teacher = request.POST.get('teacher', '').strip()
			if not teacher:
				errors['teacher'] = _(u"Teacher field is required")
			else:
				data['teacher'] = teacher

			mark = request.POST.get('mark', '').strip()
			if not mark:
				errors['mark'] = _(u'Rating field is required')
			else:
				data['mark'] = mark 

			# save ratings
			if not errors:
				ratings = Rating(**data)
				ratings.save()

				return HttpResponseRedirect(
					u'%s?status_message=%s' % (reverse('ratings'), _(u'The rating added successfully!')))

			else:
				# render form with errors and previous user input
				return render(request, 'students/ratings_add.html',
					{'students': Student.objects.all().order_by('last_name'),
					'errors': errors})

		elif request.POST.get('cancel_button') is not None:
			# redirect to the ratings page on cancel button
			return HttpResponseRedirect(
				u'%s?status_message=%s' % (reverse('ratings'), _(u'The rating add is calceled!')))
	else:
		# initial form render
		return render(request, 'students/ratings_add.html',
				{'students': Student.objects.all().order_by('last_name')})  


class RatingUpdateForm(ModelForm):
	class Meta:
		model = Rating
		fields = '__all__'

	def __init__(self, *args, **kwargs):
		super(RatingUpdateForm, self).__init__(*args, **kwargs)

		self.helper = FormHelper(self)

		# set form tag attributes
		self.helper.form_action = reverse(
			'ratings_edit', kwargs={'pk': kwargs['instance'].id})

		self.helper.form_method = 'POST'
		self.helper.form_class = 'form-horizontal'

		# set form field properties
		self.helper.help_text_inline = True
		self.helper.html5_required = True
		self.helper.label_class = 'col-sm-2 control-label'
		self.helper.field_class = 'col-sm-4'

		# add buttons
		self.helper.layout.append(FormActions(
			Submit('add_button', _(u'Save'), css_class='btn btn-primary'), 
			Submit('cancel_button', _(u'Cancel'), css_class='btn btn-link')))



class RatingUpdateView(Dispatch, UpdateView):
	model = Rating
	template_name = 'students/ratings_edit.html'
	form_class = RatingUpdateForm

	def get_success_url(self):
		return u'%s?status_message=%s' % (reverse('ratings'), _(u'The rating updated successfully!'))

	def post(self, request, *args, **kwargs):
		if request.POST.get('cancel_button'):
			return HttpResponseRedirect(
				u'%s?status_message=%s' % (reverse('ratings'), _(u'The rating update is canceled!')))
		else:
			return super(RatingUpdateView, self).post(request, *args, **kwargs)

class RatingDeleteView(Dispatch, DeleteView):
	model = Rating
	template_name = 'students/ratings_confirm_delete.html'

	def get_success_url(self):
		return u'%s?status_message=%s' % (reverse('ratings'), _(u'The rating deleted successfully!'))