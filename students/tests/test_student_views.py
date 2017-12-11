
from datetime import datetime
from django.core.urlresolvers import reverse

from django.test import TestCase, Client

from students.models.students import Student
from students.models.groups import Group

class TestStudentList(TestCase):

	def setUp(self):
		# create 2 groups
		group1, created = Group.objects.get_or_create(
			title='ABC-1')
		group2, created = Group.objects.get_or_create(
			title='ABC-2')

		# create 4 students: 1 for group1 and 3 for group2
		Student.objects.get_or_create(
			first_name='Andrii',
			last_name=u'Kobryk',
			birthday=datetime.today(),
			ticket='1234',
			students_group=group1)
		Student.objects.get_or_create(
			first_name=u'Jon',
			last_name=u'Snow',
			birthday=datetime.today(),
			ticket='1214',
			students_group=group2)
		Student.objects.get_or_create(
			first_name=u'Jorah',
			last_name=u'Mormont',
			birthday=datetime.today(),
			ticket='4434',
			students_group=group2)
		Student.objects.get_or_create(
			first_name=u'Ned',
			last_name=u'Stark',
			birthday=datetime.today(),
			ticket=u'3234',
			students_group=group2)

		# remember test browser
		self.client = Client()

		# remember url to our homepage
		self.url = reverse('home')

	def test_students_list(self):
		# make a request to the server to get a homepage page
		response = self.client.get(self.url)

		# have we received OK status from the server?
		self.assertEqual(response.status_code, 200)

		# do we have student name on a page?
		self.assertIn('Jon', response.content)

		# do we have a link to the student edit form?
		#self.assertIn(reverse('students_edit',
		#	kwargs={'pk': Student.objects.all()[0].id}), response.content)

		# ensure we got 3 students, pagination limit is 3
		self.assertEqual(len(response.context['students']), 3)