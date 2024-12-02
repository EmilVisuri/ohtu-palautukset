KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, koko):
        return [0] * koko
    
    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        if kapasiteetti is None:
            self.kapasiteetti = KAPASITEETTI
        elif not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Väärä kapasiteetti")  # heitin vaan jotain :D
        else:
            self.kapasiteetti = kapasiteetti

        if kasvatuskoko is None:
            self.kasvatuskoko = OLETUSKASVATUS
        elif not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("kapasiteetti2")  # heitin vaan jotain :D
        else:
            self.kasvatuskoko = kasvatuskoko

        self.ljono = self._luo_lista(self.kapasiteetti)

        self.alkioiden_lkm = 0

    def kuuluu(self, n):
        return n in self.ljono[:self.alkioiden_lkm]

    def lisaa(self, n):
        if self.kuuluu(n):
            return False

        if self.alkioiden_lkm == len(self.ljono):
            self._kasvata_taulukkoa()

        self.ljono[self.alkioiden_lkm] = n
        self.alkioiden_lkm += 1
        return True
    
    def _kasvata_taulukkoa(self):
        uusi_lista = self._luo_lista(len(self.ljono) + self.kasvatuskoko)
        self.kopioi_lista(self.ljono, uusi_lista)
        self.ljono = uusi_lista

    def poista(self, n):
        if not self.kuuluu(n):
            return False

        index = self.ljono.index(n)
        for i in range(index, self.alkioiden_lkm - 1):
            self.ljono[i] = self.ljono[i + 1]

        self.alkioiden_lkm -= 1
        self.ljono[self.alkioiden_lkm] = 0
        return True

    def kopioi_lista(self, vanha, uusi):
        uusi[:len(vanha)] = vanha

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        return self.ljono[:self.alkioiden_lkm]

    @staticmethod
    def yhdiste(a, b):
        tulos = IntJoukko()
        for numero in a.to_int_list() + b.to_int_list():
            tulos.lisaa(numero)
        return tulos
    
    @staticmethod
    def leikkaus(a, b):
        tulos = IntJoukko()
        for numero in a.to_int_list():
            if numero in b.to_int_list():
                tulos.lisaa(numero)
        return tulos

    @staticmethod
    def erotus(a, b):
        tulos = IntJoukko()
        for numero in a.to_int_list():
            if numero not in b.to_int_list():
                tulos.lisaa(numero)
        return tulos

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        return "{" + ", ".join(map(str, self.ljono[:self.alkioiden_lkm])) + "}"
