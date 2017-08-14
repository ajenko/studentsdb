# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.core.urlresolvers import reverse
from django.forms import ModelForm, ValidationError

from models.students import Student
from models.groups import Group
from models.exams import Exam
from models.ratings import Rating



class StudentFormAdmin(ModelForm):

	def clean_students_group(self):
		"""Check if student is a leader in any of groups.
		If yes, then ensure it`s the same as a selected gpoup."""

		# get group where the current student is a leader 
		groups = Group.objects.filter(leader = self.instance)
		if len(groups) > 0 and self.cleaned_data['students_group'] != groups[0]:
			raise ValidationError(u'Студент є старостою іншої групи', code = 'invalid')

		return self.cleaned_data['students_group']




class StudentAdmin(admin.ModelAdmin):
	list_display = ['last_name', 'first_name', 'ticket', 'students_group']
	list_display_links = ['last_name', 'first_name']
	list_editable = ['students_group']
	ordering = ['last_name']
	list_filter = ['students_group']
	list_per_page = 10
	search_fields = ['last_name', 'first_name', 'middle_name', 'ticket', 'notes']

	form = StudentFormAdmin

	def view_on_site(self, obj):
		return reverse('students_edit', kwargs = {'pk': obj.id})


# Register your models here.

admin.site.register(Student, StudentAdmin)
admin.site.register(Group)
admin.site.register(Exam)
admin.site.register(Rating)
