from __future__ import unicode_literals
from django.utils.translation import ugettext as _

from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader	
from ..models.groups import Group
from ..models.students import Student

from django.views.generic import UpdateView, DeleteView, CreateView
from django.forms import ModelForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.bootstrap import FormActions

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from ..util import paginate, get_current_group 
# Create your views here.

# Views for Groups
def groups_list(request):

	# check if we need to show only one group in groups
	current_group = get_current_group(request)
	if current_group:
		groups = Group.objects.filter(title=current_group)
	else:
		# otherwise show all groups
		groups = Group.objects.all()
	

	# try to order groups list 
	order_by = request.GET.get('order_by', '')
	if order_by in ('id', 'title', 'leader'):
		groups = groups.order_by(order_by)
		if request.GET.get('reverse', '') == '1':
			groups = groups.reverse()


	# apply pagination
	context = paginate(groups, 10, request, {},
		var_name = 'groups')
	
	return render(request, 'students/groups_list.html', context)

def groups_add(request):
	# was form posted?
	if request.method == "POST":
		# was form add button clicked?
		if request.POST.get('add_button') is not None:
			# errors collection 
			errors = {}
			# validate student data will go here
			data = {'notes': request.POST.get('notes')}

			# validate user input 
			title = request.POST.get('title', '').strip()
			if not title:
				errors['title'] = _(u"Title field is required")
			else:
				data['title'] = title

			leader = request.POST.get('leader', '').strip()
			if not leader:
				errors['leader'] = _(u"Leader field is required")
			else:
				leaders = Student.objects.filter(pk=leader)
				if len(leaders) != 1:
					errors['leader'] = _(u'Choose the correct leader')
				else:	
					data['leader'] = leader[0]

			if not errors:
					group = Group(**data)
					group.save()
				
					return HttpResponseRedirect(
						u'%s?status_message=%s'% (reverse('groups'), _(u'The group {0} added successfully!').format(title)))
			else:
				# render form with errors and previous user input 
				return render(request, 'students/groups_add.html',
					{'leaders': Student.objects.all().order_by('last_name'),
					 'errors': errors})

		elif request.POST.get('cancel_button') is not None:
			# redirect to home page on cancel button
			return HttpResponseRedirect(
				u'%s?status_message=%s' % (reverse('groups'), _(u'The group add is canceled!')))

	else:
		# initial form render
		return render(request, 'students/groups_add.html',
			{'leaders': Student.objects.all().order_by('last_name')})


class GroupAddForm(ModelForm):
	class Meta: 
		model = Group
		fields = '__all__'
		# exclude = ('',)

	def __init__(self, *args, **kwargs):
		super(GroupAddForm, self).__init__(*args, **kwargs)

		self.helper = FormHelper(self)

		# set the form tag attributes

		self.helper.form_action = reverse('groups_add')
		self.helper.form_method = 'POST'
		self.helper.form_class = 'form-horizontal'

		# set the form field properties
		self.helper.help_text_inline = True
		self.helper.html5_required = True
		self.helper.label_class = 'col-sm-2 control-label'
		self.helper.field_class = 'col-sm-4'

		# add buttons
		self.helper.layout.append(FormActions(
			Submit('add_button', _(u'Save'), css_class = "btn btn-primary"), 
			Submit('cancel_button', _(u'Cancel'), css_class = "btn btn-link")))

class GroupAddView(CreateView):
	model = Group
	template_name = 'students/groups_add_class.html'
	form_class = GroupAddForm

	def get_success_url(self):
		return u'%s?status_message=%s' % (reverse('groups'), _(u'The group added successfully!'))

	def post(self, request, *args, **kwargs):
		if request.POST.get('cancel_button'):
			return HttpResponseRedirect(u'%s?status_message=%s' % (reverse('groups'), _(u'The group add is canceled!')))
		else:
			return super(GroupAddView, self).post(request, *args, **kwargs)



class GroupUpdateForm(ModelForm):
	class Meta: 
		model = Group
		fields = '__all__'

	def __init__(self, *args, **kwargs):
		super(GroupUpdateForm, self).__init__(*args, **kwargs)

		self.helper = FormHelper(self)

		# set the form tag attributes

		self.helper.form_action = reverse(
			'groups_edit', kwargs={'pk': kwargs['instance'].id})
		
		self.helper.form_method = 'POST'
		self.helper.form_class = 'form-horizontal'

		# set the form field properties
		self.helper.help_text_inline = True
		self.helper.html5_required = True
		self.helper.label_class = 'col-sm-2 control-label'
		self.helper.field_class = 'col-sm-4'

		# add buttons
		self.helper.layout.append(FormActions(
			Submit('add_button', _(u'Save'), css_class = "btn btn-primary"), 
			Submit('cancel_button', _(u'Cancel'), css_class = "btn btn-link")
			))




class GroupUpdateView(UpdateView):
	model = Group
	template_name = 'students/groups_edit.html'
	form_class = GroupUpdateForm

	def get_success_url(self):
		return u'%s?status_message=%s' % (reverse('groups'), _(u'The group updated successfully!'))

	def post(self, request, *args, **kwargs):
		if request.POST.get('cancel_button'):
			return HttpResponseRedirect(u'%s?status_message=%s' % (reverse('groups'), _(u'The group update is canceled!')))
		else:
			return super(GroupUpdateView, self).post(request, *args, **kwargs)


class GroupDeleteView(DeleteView):
	model = Group
	template_name = 'students/groups_confirm_delete.html'

	def get_success_url(self):
		return u'%s?status_message=%s' % (reverse('groups'), _(u'The group deleted successfully!'))