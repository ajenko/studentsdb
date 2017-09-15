# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
from django.db import models

class Rating(models.Model):
	""" Rating model """
	
	class Meta(object):
		verbose_name = _(u'Rating')
		verbose_name_plural = _(u'Ratings')

	student = models.ForeignKey('Student',
		max_length = 256,
		blank = False,
		verbose_name = _(u'Student'))
	
	date_time = models.DateTimeField(
		verbose_name = _(u'Date, time'),
		blank = False) 
	
	subject = models.CharField(
		max_length = 256,
		blank = False,
		verbose_name = _(u'Subject'))
	
	teacher = models.CharField(
		verbose_name = _(u'Teacher'),
		blank = False,
		max_length = 256)
	
	mark = models.CharField(
		verbose_name = _(u'Rating'),
		max_length = 3,
		blank = False)

	notes = models.TextField(
		blank = True,
		verbose_name = _(u'Notes'))

	def __unicode__(self):
	 	if self.mark:
	 		return u"%s %s" % (self.student, self.subject)
