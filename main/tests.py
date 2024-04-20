from django.test import TestCase

# simple sample test
class SimpleTest(TestCase):
    def test_addition(self):
        self.assertEqual(1 + 1, 2)