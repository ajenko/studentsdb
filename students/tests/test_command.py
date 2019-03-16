from django.test import TestCase
from django.core.management import call_command
from django.utils.six import StringIO


class STCountTest(TestCase):
    """ Test stcount command """

    fixtures = ['students_test_data.json']

    def test_command_output(self):
        # prepare output file for command
        out = StringIO()

        # call our command
        call_command('stcount', 'student', 'group', 'user', 'exam', stdout=out)

        # get command output
        result = out.getvalue()

        # check if we get proper number of objects in the database
        self.assertIn('Number of students in a database: 4', result)
        self.assertIn('Number of groups in a database: 2', result)
        self.assertIn('Number of users in a database: 1', result)
        self.assertIn('Number of exams in a database: 0', result)
