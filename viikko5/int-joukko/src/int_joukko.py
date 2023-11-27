KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, koko):
        return [0] * koko
    
    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):
        if not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Väärä kapasiteetti")
        if not isinstance(kasvatuskoko, int) or kasvatuskoko < 0:
            raise Exception("Väärä kasvatuskoko")
        self.ljono = [0] * kapasiteetti
        self.kasvatuskoko = kasvatuskoko
        self.alkioiden_lkm = 0

    def kuuluu(self, numero):
        return numero in self.ljono
        

    def lisaa(self, n):
        if not self.kuuluu(n):
            if self.alkioiden_lkm == len(self.ljono):
                self.ljono += [0] * self.kasvatuskoko
            self.ljono[self.alkioiden_lkm] = n
            self.alkioiden_lkm += 1
            return True
        return False


    def poista(self, n):
        if self.kuuluu(n):
            self.ljono.remove(n)
            self.alkioiden_lkm -= 1
            return True
        return False

    def kopioi_lista(self, a, b):
        for i in range(0, len(a)):
            b[i] = a[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        taulu = self._luo_lista(self.alkioiden_lkm)

        for i in range(0, len(taulu)):
            taulu[i] = self.ljono[i]

        return taulu

    @staticmethod
    def yhdiste(a, b):
        yhdiste = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for alkio in a_taulu:
            yhdiste.lisaa(alkio)

        for alkio in b_taulu:
            yhdiste.lisaa(alkio)

        return yhdiste

    @staticmethod
    def leikkaus(a, b):
        leikkaus = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for alkio_a in a_taulu:
            for alkio_b in b_taulu:
                if alkio_a == alkio_b:
                    leikkaus.lisaa(alkio_b)

        return leikkaus

    @staticmethod
    def erotus(a, b):
        erotus = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for alkio in a_taulu:
            erotus.lisaa(alkio)

        for alkio in b_taulu:
            erotus.poista(alkio)

        return erotus
    

    def __str__(self):
        return_value = []
        for alkio in self.ljono:
            if alkio == 0:
                continue
            return_value.append(str(alkio))
        
        return f"{{{', '.join(return_value)}}}"

