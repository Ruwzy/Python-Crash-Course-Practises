import unittest
from city_functions import city_country


class CitynameTestCase(unittest.TestCase):
    """test city_function.py"""

    def test_city_country(self):
        neat_cityname = city_country('santiago', 'chile')
        self.assertEqual(neat_cityname, 'Santiago, Chile')

    def test_city_country_population(self):
        neat_cityname = city_country('santiago', 'chile', population_num=5000000)
        self.assertEqual(neat_cityname, 'Santiago, Chile - population 5000000')


unittest.main()
