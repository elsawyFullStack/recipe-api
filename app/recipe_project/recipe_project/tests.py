from django.test import TestCase
from recipe_project.recipe_project.calc import add

class CalcTests(TestCase):
    def test_add(self):
        self.assertEqual(add(10,2), 12)
