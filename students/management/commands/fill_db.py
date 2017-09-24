# _*_ coding: utf-8 _*_ 

from django.core.management.base import BaseCommand

from students.models.students import Student
from students.models.groups import Group
from django.contrib.auth.models import User
from random import randrange, randint
from datetime import datetime, date

class Command(BaseCommand):
	help = "Creates a specified number of objects with random parameters. \
	Number must be in range 1..99" 

	models = (('student', Student), ('group', Group), ('user', User))

	def add_arguments(self, parser):
		parser.add_argument(
			'--student',
			action='store',
			dest='student',
			default=False,
			help='Count of "student" objects',)
		parser.add_argument(
			'--group',
			action='store',
			dest='group',
			default=False,
			help='Count of "group" objects')
		parser.add_argument(
			'--user',
			action='store',
			dest='user',
			default=False,
			help='Count of "user" object')

	def handle(self, *args, **options):
		# check here: 0 < count < 100, count of objects is integer
		for name, model in self.models:
			if options.get(name) != None:
				count = options[name]
				try:
					count = int(count)
				except:
					raise ValueError("Number of '%s' objects must be an integer!"
						% name)
				if not 0 < count < 100:
					raise ValueError("Number of '%s' objects must be in range 1..99!"
						% name)

		for name, model in self.models:
			if options[name]:
				count = int(options[name])
				while count > 0:
					self._add_objects_to_db(name)
					count -= 1

	def _random_value(self, value=''):
		return value + str(randrange(10000))


	def _add_objects_to_db(self, name):
		if name == 'student':
			student = Student(
				first_name=self._random_value('first_name'), 
				last_name=self._random_value('last_name'), 
				ticket=self._random_value(),
				student_group=Group.objects.all()[randint(0, Group.objects.count()-1)], 
				birthday=datetime.today(),
				)
			student.save()

		if name == 'group':
			group = Group(
				title=self._random_value('title'),
				notes='notes about group')
			group.save()

		if name == 'user':
			user = User(
				username=self._random_value('username'), 
				first_name=self._random_value('first_name'), 
				last_name=self._random_value('last_name'), 
				email=self._random_value('email') + '@example.com', 
				)

			# User model have an unique field 'username'
			# Generated 'username' can be not unique
			# 	in compare with existing objects.
			# In case of exception repeat creating object 'user'
			try:
				user.save()
			except:
				self._add_objects_to_db(name)



