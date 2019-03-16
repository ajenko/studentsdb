# -*- coding: utf-8 -*-

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
            first_name='First Name1',
            last_name='Last Name1',
            birthday=datetime.today(),
            ticket='10',
            students_group=group1)
        Student.objects.get_or_create(
            first_name='First Name2',
            last_name='Last Name2',
            birthday=datetime.today(),
            ticket='20',
            students_group=group2)
        Student.objects.get_or_create(
            first_name='First Name3',
            last_name='Last Name3',
            birthday=datetime.today(),
            ticket='30',
            students_group=group2)
        Student.objects.get_or_create(
            first_name='First Name4',
            last_name='Last Name4',
            birthday=datetime.today(),
            ticket='40',
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
        self.assertIn('First Name1', response.content)

        # do we have a link to the student edit form?

        # TODO: ascii codec problem !!!
        # self.assertIn(reverse('students_edit',
        #   kwargs={'pk': Student.objects.all()[0].id}), response.content)

        # ensure we got 3 students, pagination limit is 3
        self.assertEqual(len(response.context['students']), 3)

    def test_current_group(self):
        # set group1 as currently a currently selected group
        group = Group.objects.filter(title='ABC-1')[0]
        self.client.cookies['current_group'] = group.id

        # make request to the server to get a homepage
        response = self.client.get(self.url)

        # in the group1 we have only 1 student
        self.assertEqual(len(response.context['students']), 1)

    def test_order_by(self):
        # set order by Last Name
        response = self.client.get(self.url, {'order_by': 'last_name'})

        # now check if we got a proper order
        students = response.context['students']
        self.assertEqual(students[0].last_name, 'Last Name1')
        self.assertEqual(students[1].last_name, 'Last Name2')
        self.assertEqual(students[2].last_name, 'Last Name3')

    def test_reverse_order_by(self):

        # order students by ticket in a reverse order
        response = self.client.get(
            self.url, {'order_by': 'ticket', 'reverse': '1'}
            )
        # check if we got a proper order
        students = response.context['students']
        self.assertEqual(students[0].last_name, 'Last Name4')
        self.assertEqual(students[1].last_name, 'Last Name3')
        self.assertEqual(students[2].last_name, 'Last Name2')

    def test_pagination(self):
        # navigate to third page with students
        response = self.client.get(self.url, {'page': '2'})

        self.assertEqual(response.context['is_paginated'], True)
        self.assertEqual(len(response.context['students']), 1)
        self.assertEqual(response.context['students'][0].last_name, 'Last Name4')
