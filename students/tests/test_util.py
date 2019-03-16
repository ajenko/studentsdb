from datetime import datetime

from django.test import TestCase
from django.http import HttpRequest


from students.models.students import Student
from students.models.groups import Group
from students.util import get_current_group


class UtilTestCase(TestCase):
    """ Test functions from util module """

    def setUp(self):
        # create 2 groups
        group1, created = Group.objects.get_or_create(
            id=1,
            title='Group1')
        group2, created = Group.objects.get_or_create(
            id=2,
            title='Group2')
        # create 2 students
        student1, created = Student.objects.get_or_create(
            id=1,
            first_name='Andrii',
            last_name='Kobryk',
            birthday=datetime.today(),
            ticket='1234',
            students_group=group1)

        # set a student as a leader for 'group1'

    def test_get_current_group(self):
        # prepate a request object to pass to an utility function
        request = HttpRequest()

        # test with no group set in a coookie
        request.COOKIES['current_group'] = ''
        self.assertEqual(None, get_current_group(request))

        # test with an invalid group id
        request.COOKIES['current_group'] = '12345'
        self.assertEqual(None, get_current_group(request))

        # test with a proper group identificator
        group = Group.objects.filter(title='Group1')[0]
        request.COOKIES['current_group'] = str(group.id)
        self.assertEqual(group, get_current_group(request))
