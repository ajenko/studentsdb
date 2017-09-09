# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

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
		blank = False,
		) 
	
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
