# -*- coding: utf-8 -*-
from django.test import TestCase
from students.models.students import Student
from students.models.groups import Group
from students.models.exams import Exam
from students.models.ratings import Rating

try:
    UNICODE_EXISTS = bool(type(unicode))
except NameError:
    def unicode(s):
        return str(s)


class ModelTests(TestCase):
    """ Test of student`s,
                groups`s,
                exam`s,
                rating`s model """

    def test_unicode(self):
        student = Student(first_name='Test', last_name='Student')
        self.assertEqual(unicode(student), u'Test Student')

        group = Group(title="Demo Title", leader=student)
        self.assertEqual(unicode(group), u'Demo Title')

        exam = Exam(subject='Test Subject', group=group)
        self.assertEqual(unicode(exam), u'Test Subject Demo Title')

        rating = Rating(student=student, subject='Test Subject', mark='100')
        self.assertEqual(unicode(rating), u'Test Student Test Subject')
