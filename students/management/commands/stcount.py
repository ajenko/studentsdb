from django.core.management.base import BaseCommand
from students.models.students import Student
from students.models.groups import Group
from django.contrib.auth.models import User
from students.models.exams import Exam


class Command(BaseCommand):
    help = 'Prints to console number of student related objects in a database'

    def add_arguments(self, parser):
        parser.add_argument('student')
        parser.add_argument('group')
        parser.add_argument('user')
        parser.add_argument('exam')

    models = (('student', Student), ('group', Group), ('user', User), ('exam', Exam))

    def handle(self, *args, **options):
        for name, model in self.models:
            if name in options:
                self.stdout.write('Number of %ss in a database: %d' % (name, model.objects.count()))
