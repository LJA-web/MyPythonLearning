import imp
import unittest


import unittest
from city_functions import getCityCountry

class CityTestCase(unittest.TestCase):
    """ 测试city_functions.py """
    
    def test_getCityCountry(self):
        cityCountry = getCityCountry('santiago', 'chile')
        self.assertEqual(cityCountry, 'santiago, chile')
    
    def test_getCityCountryPopulation(self):
        cityCountry = getCityCountry('santiago', 'chile', '5000000')
        self.assertEqual(cityCountry, 'santiago, chile - population 5000000')

unittest.main()