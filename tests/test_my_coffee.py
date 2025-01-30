from unittest import TestCase, main
from coffee.my_coffee import drink_coffee

def TestCoffee(TestCase):

    def test_drink_coffee_1(self):
        c = drink_coffee()
        self.assertEqual(c, 'caffiene')