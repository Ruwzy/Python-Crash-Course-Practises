import unittest
from Employee import Employee


class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.test_one = Employee('lazada', 'Hola', 25000)

    def test_give_default_raise(self):
        self.test_one.give_raise()
        self.assertEqual(self.test_one.an_salary, 30000)

    def test_tive_custom_raise(self):
        self.test_one.give_raise(1000)
        self.assertEqual(self.test_one.an_salary, 26000)


unittest.main()