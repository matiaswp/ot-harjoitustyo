import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti
class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)

    def test_alustetut_rahat_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_alustetut_maukkaatlounaat_oikein(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_alustetut_edullisetlounaat_oikein(self):
        self.assertEqual(self.kassapaate.edulliset, 0)

    """Kassapäätteen käteismaksun edulliset testit"""

    def test_syo_kateisella_edullisesti_nostaa_saldoa(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)

    def test_syo_kateisella_edullisesti_palauttaa_oikean_vaihdon(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(250), 10)
    
    def test_syo_kateisella_edullisesti_nostaa_edullisten_maaraa(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_riittamaton_raha_edullista_ostaessa_ei_kasvata_saldoa(self):
        self.kassapaate.syo_edullisesti_kateisella(50)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_riittamaton_raha_edullista_ostaessa_palauttaa_kaikki_rahat(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(50), 50)

    def test_riittamaton_raha_edullista_ostaessa_ei_kasvata_myytyja(self):
        self.kassapaate.syo_edullisesti_kateisella(50)
        self.assertEqual(self.kassapaate.edulliset, 0)

    """Kassapäätteen käteismaksun maukkaat testit"""

    def test_syo_kateisella_maukkaasti_nostaa_saldoa(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)

    def test_syo_kateisella_maukkaasti_palauttaa_oikean_vaihdon(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(410), 10)
    
    def test_syo_kateisella_maukkaasti_nostaa_edullisten_maaraa(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_riittamaton_raha_maukkaasti_ostaessa_ei_kasvata_saldoa(self):
        self.kassapaate.syo_maukkaasti_kateisella(50)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_riittamaton_raha_maukkaasti_ostaessa_palauttaa_kaikki_rahat(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(50), 50)

    def test_riittamaton_raha_maukkaasti_ostaessa_ei_kasvata_myytyja(self):
        self.kassapaate.syo_maukkaasti_kateisella(50)
        self.assertEqual(self.kassapaate.edulliset, 0)

    """Kassapäätteen korttimaksun edulliset testit"""

    def test_edullinen_kortti_osto_veloittaa_jos_rahaa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(str(self.maksukortti), "saldo: 7.6")

    def test_edullinen_kortti_osto_palauttaa_true_jos_rahaa(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), True)

    def test_edullinen_kortti_ostossa_tarpeeksi_rahaa_nostetaan_myytyja(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 1)
    
    def test_edullinen_jos_ei_tarpeeksi_rahaa_kortin_saldo_ei_muutu(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(str(self.maksukortti), "saldo: 0.4")

    def test_edullinen_jos_ei_tarpeeksi_rahaa_myytyjen_maara_ei_muutu(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 4)

    def test_edullinen_jos_ei_tarpeeksi_rahaa_kortilla_palauttaa_false(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), False)
    
    def test_edullinen_kortti_osto_ei_muuta_kassan_raha_maaraa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    """Kassapäätteen korttimaksun maukkaat testit"""

    def test_maukas_kortti_osto_veloittaa_jos_rahaa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(str(self.maksukortti), "saldo: 6.0")

    def test_maukas_kortti_osto_palauttaa_true_jos_rahaa(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), True)

    def test_maukas_kortti_ostossa_tarpeeksi_rahaa_nostetaan_myytyja(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)
    
    def test_maukas_jos_ei_tarpeeksi_rahaa_kortin_saldo_ei_muutu(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(str(self.maksukortti), "saldo: 2.0")

    def test_maukas_jos_ei_tarpeeksi_rahaa_myytyjen_maara_ei_muutu(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 2)

    def test_maukas_jos_ei_tarpeeksi_rahaa_kortilla_palauttaa_false(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), False)
    
    def test_maukas_kortti_osto_ei_muuta_kassan_raha_maaraa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    """Kortin lataus nostaa saldoja testi"""

    def test_rahan_lataus_nostaa_kortin_saldoa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 10)
        self.assertEqual(str(self.maksukortti), "saldo: 10.1")
    
    def test_rahan_lataus_nostaa_kassan_rahamaaraa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 10)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100010)

    def test_rahan_lataus_palauttaa_tyhjan(self):
        self.assertEqual(self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -1), None)