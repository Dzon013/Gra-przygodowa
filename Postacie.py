class Bohater:
    def __init__(self, imie, zdrowie, sila, punkty):
        self.imie = imie
        self.zdrowie = zdrowie
        self.sila = sila
        self.punkty = punkty

    def atakuj(self, przeciwnik):
        obrazenia = self.sila
        przeciwnik.zdrowie = przeciwnik.zdrowie - obrazenia
        print(f"{self.imie} zaatakował {przeciwnik.imie} i zadał {obrazenia} obrażeń!")
        if przeciwnik.zdrowie <= 0:
            print(f"{przeciwnik.imie} został pokonany!")


class Przeciwnik:
    def __init__(self, imie, zdrowie, sila, punkty):
        self.imie = imie
        self.zdrowie = zdrowie
        self.sila = sila
        self.xp = punkty

    def atakuj(self, bohater):
        obrazenia = self.sila
        bohater.zdrowie = bohater.zdrowie - obrazenia
        print(f"{self.imie} zaatakował {bohater.imie} i zadał {obrazenia} obrażeń!")
        print(f"{bohater.imie}:\nzdrowie: {bohater.zdrowie}")
        print(f"{self.imie}:\nzdrowie: {self.zdrowie}")
        if bohater.zdrowie <= 0:
            print(f"{bohater.imie} został pokonany!")
