from KPS.kps_parempi_tekoaly import KPSParempiTekoaly
from KPS.kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from KPS.kps_tekoaly import KPSTekoaly


class KPS_tehdas:
    
    @staticmethod
    def pelaajaa_vastaan():
        return KPSPelaajaVsPelaaja()
    
    @staticmethod
    def tekoalya_vastaan(tekoaly):
        return KPSTekoaly(tekoaly)
    
    @staticmethod
    def parempaa_tekoalya_vastaan(tekoaly):
        return KPSParempiTekoaly(tekoaly)
    
