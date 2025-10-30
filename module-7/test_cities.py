# Kristopher Duda. October 26, 2025. Assignment 7.2: Test Cases.
# This short program tests the city_country() function in the city_functions.py file 
# using unittest. It creates a method called test_city_country() to verify
# that calling the function with values such as 'santiago' and 'chile' results in the
# correct string output.


import unittest
from city_functions import city_country


class TestCityCountry(unittest.TestCase):
    """This class contains tests for the function city_country()."""

    def test_city_country(self):
        """Test to see if 'santiago' and 'chile' produce correct output"""
        formatted_name = city_country('santiago', 'chile')
        self.assertEqual(formatted_name, 'Santiago, Chile') # assertEqual() checks whether output matches


if __name__ == '__main__':
    unittest.main()
