from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
from django.db import models


class Group(models.Model):
    """ Group model """

    title = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=_(u"Title")
        )

    leader = models.OneToOneField(
        'Student',
        verbose_name=_(u"Leader"),
        blank=False,
        null=True,
        on_delete=models.SET_NULL
        )

    notes = models.TextField(
        blank=True,
        verbose_name=_(u"Notes"))

    class Meta(object):
        verbose_name = _(u"Group")
        verbose_name_plural = _(u"Groups")
        ordering = ['title']

    def __unicode__(self):
        if self.leader:
            return u"%s" % (self.title)
