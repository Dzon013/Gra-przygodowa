from Gra import Gra


class Ekwipunek:
    def __init__(self, ochrona, atak, cena):
        self.bohater = None
        self.ochrona = ochrona
        self.atak = atak
        self.cena = cena

    def zbrojownia(self):
        print("Witamy w zbrojowni. Co chciałbyś kupić?: ")
        print("0. Nic")
        print("1. Miecz: 120zł (+30 do obrażeń)")
        print("2. Łuk: 200zł (+100 do obrażeń)")
        print("3. Tarcza: 150zł (+ 25 do osłony)")
        print("4. Zbroja: 300zł (+ 100 do osłony)")
        print("5. Zwiększenie levela: 50zł - wzrasta o 50zł (+ 1 do level)")

        kupno = input("Podaj liczbę: ")
        if kupno == "0":
            Gra.poruszaj_sie()
        elif kupno == "1":
            if self.bohater.pieniadze < 120:
                print("Za mało punktów")
                Gra.poruszaj_sie()
            else:
                self.bohater.pieniadze = self.bohater.pieniadze - 120
                self.bohater.sila = self.bohater.sila + 30
                print("Zakupiono miecz. Zadajesz teraz więcej obrażeń")
                print(f"{self.bohater.imie}:\nzdrowie: {self.bohater.zdrowie}\nobrażenia: {self.bohater.sila}\nosłona: {self.bohater.oslona}\npunkty: {self.bohater.punkty}\nBudżet: {self.bohater.pieniadze}\nLevel {self.bohater.level}")
                Gra.poruszaj_sie()
        elif kupno == "2":
            if self.bohater.pieniadze < 200:
                print("Za mało punktów")
                Gra.poruszaj_sie()
            else:
                self.bohater.pieniadze = self.bohater.pieniadze - 200
                self.bohater.sila = self.bohater.sila + 100
                print("Zakupiono łuk. Zadajesz teraz jeszcze więcej obrażeń")
                print(f"{self.bohater.imie}:\nzdrowie: {self.bohater.zdrowie}\nobrażenia: {self.bohater.sila}\nosłona: {self.bohater.oslona}\npunkty: {self.bohater.punkty}\nBudżet: {self.bohater.pieniadze}\nLevel {self.bohater.level}")
                Gra.poruszaj_sie()
        elif kupno == "3":
            if self.bohater.pieniadze < 150:
                print("Za mało punktów")
                Gra.poruszaj_sie()
            else:
                self.bohater.pieniadze = self.bohater.pieniadze - 150
                self.bohater.oslona = self.bohater.oslona + 25
                print("Zakupiono tarczę. Możesz czuć się trochę bezpieczniej")
                print(f"{self.bohater.imie}:\nzdrowie: {self.bohater.zdrowie}\nobrażenia: {self.bohater.sila}\nosłona: {self.bohater.oslona}\npunkty: {self.bohater.punkty}\nBudżet: {self.bohater.pieniadze}\nLevel {self.bohater.level}")
                Gra.poruszaj_sie()

        elif kupno == "4":
            if self.bohater.pieniadze < 300:
                print("Za mało punktów")
                Gra.poruszaj_sie()
            else:
                self.bohater.pieniadze = self.bohater.pieniadze - 300
                self.bohater.oslona = self.bohater.oslona + 100
                print("Zakupiono zbroję. Możesz czuć się ultra bezpieczny.")
                print(f"{self.bohater.imie}:\nzdrowie: {self.bohater.zdrowie}\nobrażenia: {self.bohater.sila}\nosłona: {self.bohater.oslona}\npunkty: {self.bohater.punkty}\nBudżet: {self.bohater.pieniadze}\nLevel {self.bohater.level}")
                Gra.poruszaj_sie()

        elif kupno == "5":
            koszt = 50
            wzmocnienie = 20
            if self.bohater.pieniadze < koszt:
                print("Za mało pieniędzy")
                Gra.poruszaj_sie()
            else:
                while self.bohater.pieniadze >= koszt:
                    self.bohater.pieniadze = self.bohater.pieniadze - 50
                    self.bohater.sila = self.bohater.sila + wzmocnienie
                    self.bohater.oslona = self.bohater.oslona + wzmocnienie
                    self.bohater.zdrowie = self.bohater.zdrowie + wzmocnienie
                    koszt = koszt + 50
                    wzmocnienie = wzmocnienie + 20


class Wioska:
    def __init__(self):
        self.bohater = None
        self.self = self

    def regeneracja(self):
        regen = input("Odwiedzasz wioskę i regenerujesz zdrowie.\nTAK: Koszt: 10zł\nMAX: Koszt: 50zł\nNIE: aby wyjść:")
        if regen == "NIE":
            Gra.poruszaj_sie()
        elif regen == "TAK":
            self.bohater.zdrowie += 10
            self.bohater.pieniadze = self.bohater.pieniadze - 10
            print(f"{self.bohater.imie}:\nzdrowie: {self.bohater.zdrowie}\nobrażenia: {self.bohater.sila}\nosłona: {self.bohater.oslona}\npunkty: {self.bohater.punkty}\nBudżet: {self.bohater.pieniadze}\nLevel {self.bohater.level}")
            Gra.poruszaj_sie()
        elif regen == "Max":
            self.bohater.zdrowie += 50
            self.bohater.pieniadze = self.bohater.pieniadze - 50
            print(f"{self.bohater.imie}:\nzdrowie: {self.bohater.zdrowie}\nobrażenia: {self.bohater.sila}\nosłona: {self.bohater.oslona}\npunkty: {self.bohater.punkty}\nBudżet: {self.bohater.pieniadze}\nLevel {self.bohater.level}")
            Gra.poruszaj_sie()
