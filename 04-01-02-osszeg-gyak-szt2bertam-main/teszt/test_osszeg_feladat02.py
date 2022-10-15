from unittest import TestCase

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

import  osszeg

class TestOsszeg(TestCase):
    def test_feladat02_osszeg(self):
        aktualis = osszeg.feladat02_osszeg()
        elvart = 8.7
        self.assertEqual(elvart, aktualis, "A pozitív számok összegét helytelenül határozta meg!")
