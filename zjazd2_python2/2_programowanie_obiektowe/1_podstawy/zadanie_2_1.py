# # 1. Stwórz klase Car, której atrybutami będą kolor, rocznik, cena oraz marka.
# Klasa ta ma posiadać również metodę (funkcję) wyświetlającą w.w. dane,
# z tym, że cena ma byc po przecenie, której procent ma być podawany do
# metody jako zmienna.
# Stwórz dwa obiekty tej klasy i wykonaj na nich metode.

class Car:

    def __init__(self, kolor, rocznik, cena, marka):

        self.kolor = kolor
        self.rocznik = rocznik
        self.cena = cena
        self.marka = marka

    def wyswietl(self):
        print(f"Samochód, kolor: {self.kolor}, rocznik: {self.rocznik}, cena: {self.cena}, marka: {self.marka}")

    def oblicz_promocje(self, promocja):
        return self.cena - self.cena * promocja / 100


car1 = Car('biały', 1980, 20_000, 'Opel')
car1.wyswietl()
print(f"Cena po promocji {20}%: {car1.oblicz_promocje(20)}")

car2 = Car('czerwony', 2010, 120_000, 'Ferarri')
car2.wyswietl()
print(f"Cena po promocji {10}%: {car2.oblicz_promocje(10)}")


