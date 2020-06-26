from django.test import TestCase
from .views import home_view
import unittest


class Test(unittest.TestCase):

    def test_home_view(self):
        result = home_view(1)
        self.assertEqual(result, 1)

