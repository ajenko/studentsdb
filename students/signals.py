# _*_ coding: utf-8 _*_
import logging

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver 

from django.contrib.auth.models import User
from .models.students import Student
from .models.groups import Group
from .models.exams import Exam
from .models.ratings import Rating



# Students
# ------------------------------------------------------------------------------

@receiver(post_save, sender=Student)
def log_student_updated_added_event(sender, **kwargs):
	""" Writes information about newly added or updated student info log file """
	logger = logging.getLogger(__name__)

	student = kwargs['instance']
	if kwargs['created']:
		logger.info(u'Student added: %s %s (ID: %d)', student.first_name, student.last_name,
			student.id)
	else:
		logger.info(u'Student updated: %s %s (ID: %d)', student.first_name, student.last_name,
			student.id)

@receiver(post_delete, sender=Student)
def log_student_delete_event(sender, **kwargs):
	""" Writes information about deleted student info log file """
	logger = logging.getLogger(__name__)

	student = kwargs['instance']
	logger.info(u'Student deleted: %s %s (ID: %d)', student.first_name, student.last_name,
		student.id)


# Groups
# ------------------------------------------------------------------------------

@receiver(post_save, sender=Group)
def log_group_updated_added_event(sender, **kwargs):
	""" Writes the info about newly added or updated group info log file """ 
	logger = logging.getLogger(__name__)

	group = kwargs['instance']
	if kwargs['created']:
		logger.info(u'Group added: %s %s(ID: %s', group.title, group.leader, group.id)
	else:
		logger.info(u'Group updated: %s %s(ID: %s', group.title, group.leader, group.id)

@receiver(post_delete, sender=Group)
def log_group_delete_event(sender, **kwargs):
	""" Writes information about deleted group info log file """
	logger = logging.getLogger(__name__)

	group = kwargs['instance']
	logger.info(u'Group deleted: %s %s(ID: %s)', group.title, group.leader, group.id)


# Exams
# ------------------------------------------------------------------------------
@receiver(post_save, sender=Exam)
def log_exam_updated_added_event(sender, **kwargs):
	""" Writes information about newly added or updated exam info log file """
	logger = logging.getLogger(__name__)

	exam = kwargs['instance']
	if kwargs['created']:
		logger.info(u'Exam added: %s %s (ID: %d)', exam.subject, exam.group,
			exam.id)
	else:
		logger.info(u'Student updated: %s %s (ID: %d)', exam.subject, exam.group,
			exam.id)

@receiver(post_delete, sender=Exam)
def log_exam_delete_event(sender, **kwargs):
	""" Writes information about deleted exam info log file """
	logger = logging.getLogger(__name__)

	exam = kwargs['instance']
	logger.info('Exam deleted: %s %s (ID: %d)', exam.subject, exam.group,
			exam.id)
# Ratings
# ------------------------------------------------------------------------------
@receiver(post_save, sender=Rating)
def log_rating_updated_added_event(sender, **kwargs):
	""" Writes information about newly added or updated rating info log file """
	logger = logging.getLogger(__name__)

	rating = kwargs['instance']
	if kwargs['created']:
		logger.info(u'Rating added: %s %s (ID: %d)', rating.student, rating.subject, rating.id)
	else:
		logger.info(u'Rating updated: %s %s (ID: %d)', rating.student, rating.subject, rating.id)

@receiver(post_delete, sender=Rating)
def log_rating_delete_event(sender, **kwargs):
	""" Writes information about deleted rating info log file """
	logger = logging.getLogger(__name__)

	rating = kwargs['instance']
	logger.info(u'Rating deleted: %s %s (ID: %d)', rating.student, rating.subject, rating.id)

# Users
# ------------------------------------------------------------------------------
@receiver(post_save, sender=User)
def log_user_updated_added_event(sender, **kwargs):
	""" Writes information aboit newly added or updated user info log file """ 
	logger = logging.getLogger(__name__)

	user = kwargs['instance']
	if kwargs['created']:
		logger.info(u'User added: %s %s (ID: %d', user.username, user.email, user.id)
	else:
		logger.info(u'User updated: %s %s (ID: %d)', user.username, user.email, user.id)

@receiver(post_delete, sender=User)
def log_user_delete_event(sender, **kwargs):
	""" Writes information about deleted user info log file """ 
	logger = logging.getLogger(__name__)

	user = kwargs['instance']
	logger.info(u'User deleted: %s %s (ID: %d)', user.username, user.email, user.id)

