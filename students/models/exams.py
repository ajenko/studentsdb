# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

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