from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import get_d
class MyTestCase(TestCase):
    def test_get_d_1(self):
        self.assertEqual(get_d(2003, 2503, 17), 2946473)
    def test_get_d_2(self):
        self.assertEqual(get_d(292361466231755597564095925310764764819, 307125506157764866722739041634199200019, 65537), 21266554735539990938794214424150057032684401233730383604860243814738045553417)