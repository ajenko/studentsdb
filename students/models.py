# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Student(models.Model):
	""" Students model """

	class Meta(object):
		verbose_name = u"Студент"
		verbose_name_plural = u"Студенти"
		ordering = ['last_name']

	first_name = models.CharField(
		max_length = 256,
		blank = False,
		verbose_name = u"Ім'я")

	last_name = models.CharField(
		max_length = 256, 
		blank = False, 
		verbose_name = u"Прізвище")

	middle_name = models.CharField(
		max_length = 256,
		blank = False,
		verbose_name = u"По-батькові",
		default='')

	birthday = models.DateField(	
		blank = False,
		verbose_name = u"Дата народження",
		null = True)

	photo = models.ImageField(
		blank = True,
		verbose_name = u"Фото",
		null = True)

	ticket = models.CharField(
		max_length = 4,
		blank = False,
		verbose_name = u"Білет")

	notes = models.TextField(
		blank = True, 
		verbose_name = u"Додаткові нотатки")
	
	students_group = models.ForeignKey('Group',
		verbose_name = u'Група',
		blank = False,
		null = True,
		on_delete = models.PROTECT)
	
	def __unicode__(self):
		return u"%s %s %s" % (self.first_name, self.last_name, self.students_group)



class Group(models.Model):
	""" Group model """

	class Meta(object):
		verbose_name = u"Група"
		verbose_name_plural = u"Групи"

	title = models.CharField(
		max_length = 256,
		blank = False,
		verbose_name = u"Назва")

	leader = models.OneToOneField('Student',
		verbose_name = u"Староста",
		blank = True,
		null = True,
		on_delete = models.SET_NULL)

	notes = models.TextField(
		blank = True,
		verbose_name = u"Додаткові нотатки")
	
	def __unicode__(self):
		if self.leader:
			return u"%s" % (self.title)

class Exam(models.Model):
	""" Exam model """

	class Meta(object):
		verbose_name = u'Іспит'
		verbose_name_plural = u'Іспити'

	subject = models.CharField(
		max_length = 256,
		blank = False,
		verbose_name = u'Предмет')

	date_time = models.DateTimeField(
		verbose_name = u'Дата, час',
		blank = False,
		)

	teacher = models.CharField(
		verbose_name = u'Викладач',
		blank = False,
		max_length = 256)
	
	group = models.ForeignKey('Group',
		verbose_name = u'Група', 
		blank = False,
		null = True)

	notes = models.TextField(
		blank = True,
		verbose_name = u'Додаткові нотатки')

	def __unicode__(self):
	 	if self.group:
	 		return u"%s %s" % (self.subject, self.group)

	
class Rating(models.Model):
	""" Rating model """
	
	class Meta(object):
		verbose_name = u'Оцінка'
		verbose_name_plural = u'Оцінки'

	student = models.ForeignKey('Student',
		max_length = 256,
		blank = False)
		#verbose_name = u'Студент')
	
	date_time = models.DateTimeField(
		verbose_name = u'Дата, час',
		blank = False) 
	
	subject = models.CharField(
		max_length = 256,
		blank = False,
		verbose_name = u'Предмет')
	
	teacher = models.CharField(
		verbose_name = u'Викладач',
		blank = False,
		max_length = 256)
	
	mark = models.CharField(
		verbose_name = u'Оцінка',
		max_length = 3,
		blank = False)

	notes = models.TextField(
		blank = True,
		verbose_name = u'Додаткові нотатки')

	def __unicode__(self):
	 	if self.mark:
	 		return u"%s %s" % (self.student, self.subject)


		