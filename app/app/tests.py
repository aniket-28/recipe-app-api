from django.test import TestCase
from app.calc import add

class CalcTests(TestCase):

    def test_add(self):
        self.assertEqual(add(1, 2), 3)