from django.test import TestCase, Client, override_settings
from django.core.urlresolvers import reverse
from students.models.groups import Group
from students.models.students import Student


@override_settings(LANGUAGE_CODE='en')
class TestStudentUpdateForm(TestCase):

    fixtures = ['students_test_data.json']

    def setUp(self):
        # remember a test browser
        self.client = Client()

        # remember url to the edit form
        self.url = reverse('students_edit', kwargs={'pk': 1})

    def test_form(self):
        # login as an admin to access the student edit form
        self.client.login(username='admin', password='admin')
        # get form and check few fields there
        response = self.client.get(self.url)

        # check response status
        self.assertEqual(response.status_code, 200)

        # check a page title, few fields titles and a button on an edit form
        self.assertIn('Edit the Student', response.content)
        self.assertIn('Ticket', response.content)
        self.assertIn('Last Name', response.content)
        self.assertIn('name="add_button"', response.content)
        self.assertIn('name="cancel_button"', response.content)
        # self.assertIn(self.url, response.content)
        self.assertIn('kobryk.jpg', response.content)

    def test_success(self):
        # login as admin to access a student edit form
        self.client.login(username='admin', password='admin')

        # post form with valid data
        group = Group.objects.filter(title='Group2')[0]
        response = self.client.post(self.url, {
            'first_name': 'Updated Name', 
            'last_name': 'Updated Last Name',
            'ticket': '567',
            'students_group': group.id, 
            'birthday': '1990-11-11'}, follow=True)
        # check a response status
        self.assertEqual(response.status_code, 200)

        # test updated student details
        student = Student.objects.get(pk=1)
        self.assertEqual(student.first_name, 'Updated Name')
        self.assertEqual(student.last_name, 'Updated Last Name')
        self.assertEqual(student.ticket, '567')
        self.assertEqual(student.students_group, group)

        # check a proper redirect after a form post
        self.assertIn('The student updated successfully!', response.content)
        self.assertEqual(
            response.redirect_chain[0][0],
            '/?status_message=' + 'The%20student%20updated%20successfully!'
            )

    def test_access(self):
        # try to access a form as an anonymous user
        response = self.client.get(self.url, follow=True)

        # we have to get 200 code and a login form
        self.assertEqual(response.status_code, 200)
        # check if we`re on a login form
        self.assertIn('Login Form', response.content)
        # check redirect url
        self.assertEqual(
            response.redirect_chain[0],
            ('/users/login/?next=/students/1/edit/', 302)
            )
