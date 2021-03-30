import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)
    
    def test_kortin_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")
    
    def test_rahan_lataaminen_kasvattaa_saldoa(self):
        self.maksukortti.lataa_rahaa(25)
        self.assertEqual(str(self.maksukortti), "saldo: 0.35")

    def test_saldo_vähenee_jos_rahaa_tarpeeksi(self):
        self.assertEqual(self.maksukortti.ota_rahaa(6), True)

    def test_saldo_ei_muutu_jos_rahaa_ei_tarpeeksi(self):
        self.assertEqual(self.maksukortti.ota_rahaa(11), False)

