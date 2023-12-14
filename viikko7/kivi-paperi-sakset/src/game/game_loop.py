from KPS.kps_tehdas import KPS_tehdas
from tekoaly.tekoaly import Tekoaly
from tekoaly.tekoaly_parannettu import TekoalyParannettu

class GameLoop:
    def __init__(self) -> None:
        self._modes = {
            'a': KPS_tehdas.pelaajaa_vastaan(),
            'b': KPS_tehdas.tekoalya_vastaan(Tekoaly()),
            'c': KPS_tehdas.parempaa_tekoalya_vastaan(TekoalyParannettu(10))
        }

    def start(self):
        while True:
            print("Valitse pelataanko"
                "\n (a) Ihmistä vastaan"
                "\n (b) Tekoälyä vastaan"
                "\n (c) Parannettua tekoälyä vastaan"
                "\nMuilla valinnoilla lopetetaan"
                )

            vastaus = input()

            try:
                peli = self._modes[vastaus[-1]]
                print(
                    "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
                )
                peli.pelaa()

            except KeyError or IndexError:
                break