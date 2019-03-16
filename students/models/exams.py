from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
from django.db import models


class Exam(models.Model):
    """ Exam model """

    subject = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=_(u'Subject'))

    date_time = models.DateTimeField(
        verbose_name=_(u'Date, time'),
        blank=False,
        )

    teacher = models.CharField(
        verbose_name=_(u'Teacher'),
        blank=False,
        max_length=256)

    group = models.ForeignKey(
        'Group',
        verbose_name=_(u'Group'),
        blank=False,
        null=True
        )

    notes = models.TextField(
        blank=True,
        verbose_name=_(u'Notes')
        )

    class Meta(object):
        verbose_name = _(u'Exam')
        verbose_name_plural = _(u'Exams')
        ordering = ['group']

    def __unicode__(self):
        if self.group:
            return u"%s %s" % (self.subject, self.group)
