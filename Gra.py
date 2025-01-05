from Postacie import Przeciwnik
from Postacie import Bohater


class Gra:
    def __init__(self):
        self.bohater = None
        self.przeciwnik1 = Przeciwnik("Goblin", 30, 5, 50)
        self.przeciwnik2 = Przeciwnik("Pająk", 50, 15, 100)
        self.przeciwnik3 = Przeciwnik("Śmierć", 70, 30, 200)
        self.przeciwnik4 = Przeciwnik("Terroryści", 100, 20, 300)
        self.boss = Przeciwnik("Smok", 300, 40, 400)

    def start(self):
        print("Witaj w grze przygodowej!")
        imie = input("Jak masz na imię, bohaterze?\n")
        if imie == "admin":
            self.bohater = Bohater(imie, 1000, 1000, 10000)
            print(f"\n{imie}:\nzdrowie: {self.bohater.zdrowie}\nobrażenia: {self.bohater.sila}\npunkty: {self.bohater.punkty}")
            self.poruszaj_sie()
        else:
            self.bohater = Bohater(imie, 10, 10, 100)
            print(f"\n{imie}:\nzdrowie: {self.bohater.zdrowie}\nobrażenia: {self.bohater.sila}\npunkty: {self.bohater.punkty}")
            self.poruszaj_sie()

    def poruszaj_sie(self):
        print("\nGdzie chcesz się udać?")
        print("1. Las")
        print("2. jaskinia")
        print("3. Bliskie spotkanie z....")
        print("4. konwuj bandziorów")
        print("5. Wioska")
        print("6. Zbrojownia")
        print("7. Boss")

        wybor = input("Wybierz opcję: ")
        if wybor == "1":
            print("Wchodzisz do lasu i spotykasz przeciwnika!")
            self.walka(self.przeciwnik1)
        elif wybor == "2":
            print("Wchodzisz do jaskini i spotykasz przeciwnika!")
            self.walka(self.przeciwnik2)
        elif wybor == "3":
            print("Wstąpiłeś na cmentarz!")
            self.walka(self.przeciwnik3)
        elif wybor == "4":
            print("Idziesz ulicą i spotykasz konwuj terrorystów!")
            self.walka(self.przeciwnik4)
        elif wybor == "5":
            regen = input("Odwiedzasz wioskę i regenerujesz zdrowie.\nTAK: Koszt 10 punktów lub NIE aby wyjść: ")
            if regen == "NIE":
                self.poruszaj_sie()
            if regen == "TAK":
                self.bohater.zdrowie += 10
                self.bohater.punkty = self.bohater.punkty - 10
                print(f"{self.bohater.imie}:\nzdrowie: {self.bohater.zdrowie}\nobrażenia: {self.bohater.sila}\npunkty: {self.bohater.punkty}")
                self.poruszaj_sie()
        elif wybor == "6":
            print("Witamy w zbrojowni, co chciałbyś kupić. Mamy na stanie:\nmiecz: 120 punktów\nłuk: 200 punktów\ntarcza: 400 punktów\n")
            print(f"{self.bohater.imie}:\nzdrowie: {self.bohater.zdrowie}\nobrażenia: {self.bohater.sila}\npunkty: {self.bohater.punkty}\n")
            kupno = input(str("Jeśli chcesz opuścić zbrojownie wpisz 0: "))
            if kupno == "0":
                self.poruszaj_sie()
            elif kupno == "miecz":
                if self.bohater.punkty < 120:
                    print("Za mało punktów")
                    self.poruszaj_sie()
                else:
                    self.bohater.punkty = self.bohater.punkty - 120
                    self.bohater.sila = self.bohater.sila + 20
                    print("Zakupiono miecz. Zadajesz teraz więcej obrażeń")
                    print(f"\n{self.bohater.imie}:\nzdrowie: {self.bohater.zdrowie}\nobrażenia: {self.bohater.sila}\npunkty: {self.bohater.punkty}\n")
                    self.poruszaj_sie()
            elif kupno == "łuk":
                if self.bohater.punkty < 200:
                    print("Za mało punktów")
                    self.poruszaj_sie()
                else:
                    self.bohater.punkty = self.bohater.punkty - 200
                    self.bohater.sila = self.bohater.sila + 40
                    print("Zakupiono łuk. Zadajesz teraz jeszcze więcej obrażeń")
                    print(f"\n{self.bohater.imie}:\nzdrowie: {self.bohater.zdrowie}\nobrażenia: {self.bohater.sila}\npunkty: {self.bohater.punkty}\n")
                    self.poruszaj_sie()
            elif kupno == "tarcza":
                if self.bohater.punkty < 400:
                    print("Za mało punktów")
                    self.poruszaj_sie()
                else:
                    self.bohater.punkty = self.bohater.punkty - 400
                    self.bohater.sila = self.bohater.sila + 100
                    print("Zakupiono tarczę. Zatajesz teraz ogromne obrażenia")
                    print(f"\n{self.bohater.imie}:\nzdrowie: {self.bohater.zdrowie}\nobrażenia: {self.bohater.sila}\npunkty: {self.bohater.punkty}\n")
                    self.poruszaj_sie()
        elif wybor == "7":
            print("Uwaga! Nadchodzi BOSS!")
            self.walka(self.boss)
        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")
            self.poruszaj_sie()

    def walka(self, przeciwnik):
        while self.bohater.zdrowie > 0 and przeciwnik.zdrowie > 0:
            print("\n1. Atak")
            print("2. Ucieczka")
            wybor = input("Wybierz opcję: ")
            if wybor == "1":
                self.bohater.atakuj(przeciwnik)
                if przeciwnik.zdrowie > 0:
                    przeciwnik.atakuj(self.bohater)
            elif wybor == "2":
                print("Uciekasz z walki!")
                self.bohater.punkty = self.bohater.punkty - 10
                przeciwnik.zdrowie = przeciwnik.zdrowie + 50
                self.poruszaj_sie()
                break
            else:
                print("Nieprawidłowy wybór.")
        if self.bohater.zdrowie <= 0:
            print("Przegrałeś! Gra zakończona.")
        elif przeciwnik.zdrowie <= 0:
            print(f"Wygrałeś walkę!\n otrzymujesz {przeciwnik.xp} punktów")
            self.bohater.punkty = self.bohater.punkty + przeciwnik.xp
            print(f"\n{self.bohater.imie}:\nzdrowie: {self.bohater.zdrowie}\nobrażenia: {self.bohater.sila}\npunkty: {self.bohater.punkty}\n")
            self.poruszaj_sie()
