from unittest import TestCase

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

import  osszeg

class TestOsszeg(TestCase):
    def test_feladat04_osszeg(self):
        aktualis = osszeg.feladat04_osszeg()
        elvart = 40
        self.assertEqual(elvart, aktualis, "Az összeget helytelenül határozta meg!")
