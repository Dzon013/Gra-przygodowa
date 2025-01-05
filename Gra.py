from Postacie import Przeciwnik
from Postacie import Bohater
from Pasywne_Lokacje import Ekwipunek
from Pasywne_Lokacje import Wioska


class Gra:
    def __init__(self):
        self.bohater = None
        self.przeciwnik1 = Przeciwnik("Goblin", 30, 5, 50, 50)
        self.przeciwnik2 = Przeciwnik("Pająk", 50, 15, 100, 100)
        self.przeciwnik3 = Przeciwnik("Śmierć", 70, 30, 200, 200)
        self.przeciwnik4 = Przeciwnik("Terroryści", 100, 20, 300, 300)
        self.boss = Przeciwnik("Smok", 300, 40, 400, 400)

    def start(self):
        print("Witaj w grze przygodowej!")
        imie = input("Jak masz na imię, bohaterze?\n")
        if imie == "admin":
            self.bohater = Bohater(imie, 1000, 1000, 0, 10000, 0, 999)
            print(f"{self.bohater.imie}:\nzdrowie: {self.bohater.zdrowie}\nobrażenia: {self.bohater.sila}\nosłona: {self.bohater.oslona}\npunkty: {self.bohater.punkty}\nBudżet: {self.bohater.pieniadze}\nLevel {self.bohater.level}")
            self.poruszaj_sie()
        else:
            self.bohater = Bohater(imie, 10, 10, 0, 100, 0, 0)
            print(f"{self.bohater.imie}:\nzdrowie: {self.bohater.zdrowie}\nobrażenia: {self.bohater.sila}\nosłona: {self.bohater.oslona}\npunkty: {self.bohater.punkty}\nBudżet: {self.bohater.pieniadze}\nLevel {self.bohater.level}")
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
            Wioska.regeneracja()
        elif wybor == "6":
            Ekwipunek.zbrojownia()
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
                self.bohater.pieniadze = self.bohater.pieniadze - 10
                przeciwnik.zdrowie = przeciwnik.zdrowie + 50
                self.poruszaj_sie()
                break
            else:
                print("Nieprawidłowy wybór.")
        if self.bohater.oslona <= 0:
            if self.bohater.zdrowie <= 0:
                print("Przegrałeś! Gra zakończona.")
        elif przeciwnik.zdrowie <= 0:
            print(f"Wygrałeś walkę!\n otrzymujesz {przeciwnik.xp} punktów oraz {przeciwnik.xp}zł")
            self.bohater.punkty = self.bohater.punkty + przeciwnik.xp
            self.bohater.pieniadze = self.bohater.pieniadze + przeciwnik.xp
            print(f"{self.bohater.imie}:\nzdrowie: {self.bohater.zdrowie}\nobrażenia: {self.bohater.sila}\nosłona: {self.bohater.oslona}\npunkty: {self.bohater.punkty}\nBudżet: {self.bohater.pieniadze}\nLevel {self.bohater.level}")
            self.poruszaj_sie()


