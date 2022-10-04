from unicodedata import name
import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.firstEmployee = Employee('Stark','Tony','5000')

    def test_give_default_raise(self):
        self.assertEqual(self.firstEmployee.give_raise(),'5000')
