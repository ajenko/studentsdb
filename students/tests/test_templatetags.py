from django.template import Template, Context
from django.test import TestCase


class TemplateTagTests(TestCase):
    def test_str2ing(self):
        """ Test str2int template filter """

        out = Template(
            '{% load str2int %}'
            '{% if 40 == "40"|str2int %}'
            'it works'
            '{% endif %}'
        ).render(Context())

        # check for our addition operation result
        self.assertIn('it works', out)
