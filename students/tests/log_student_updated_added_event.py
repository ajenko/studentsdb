import logging

from django.utils.six import StringIO
from django.test import TestCase

from students.models.students import Student


class StudentSignalTests(TestCase):

    def test_log_student_updated_added_event(self):
        """ Check a logging signal 
        for a newly created student """
        out = StringIO()
        handler = logging.StreamHandler(out)
        logging.root.addHandler(handler)

        # now create a student, this should raise a new message
        # inside our logger output file

        student = Student(first_name='Test', last_name="Student1")
        student.save()

        # check an output file content
        out.seek(0)
        self.assertEqual(out.readlines()[-1], 'Student added: Test Student1 (ID: %d)\n' % student.id)

        # now update an existing student and check a last line in out
        student.ticket = '12'
        student.save()
        out.seek(0)
        self.assertEqual(out.readlines()[-1], 'Student updated: Test Student1 (ID: %d)\n' % student.id)

        # remove our handler from a root logger
        logging.root.removeHandler(handler)
