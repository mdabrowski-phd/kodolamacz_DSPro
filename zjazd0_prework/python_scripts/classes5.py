from abc import ABC, abstractmethod
import math


class Wezel(ABC):

    def __init__(self, lewy, prawy=None):
        self.lewy = lewy
        self.prawy = prawy

    @abstractmethod
    def oblicz(self):
        pass

    @abstractmethod
    def wypisz(self):
        pass


class Liczba(Wezel):

    def oblicz(self):
        return self.lewy

    def wypisz(self):
        return str(self.lewy)


class Dodaj(Wezel):

    def oblicz(self):
        return self.lewy.oblicz() + self.prawy.oblicz()

    def wypisz(self):

        napis = self.lewy.wypisz() + "\n" + self.prawy.wypisz() + "\n"
        return napis + f"{self.lewy.oblicz()} + {self.prawy.oblicz()} = {self.oblicz()}"


class Odejmij(Wezel):

    def oblicz(self):
        return self.lewy.oblicz() - self.prawy.oblicz()

    def wypisz(self):

        napis = self.lewy.wypisz() + "\n" + self.prawy.wypisz() + "\n"
        return napis + f"{self.lewy.oblicz()} - {self.prawy.oblicz()} = {self.oblicz()}"


class Mnoz(Wezel):

    def oblicz(self):
        return self.lewy.oblicz() * self.prawy.oblicz()

    def wypisz(self):

        napis = self.lewy.wypisz() + "\n" + self.prawy.wypisz() + "\n"
        return napis + f"{self.lewy.oblicz()} * {self.prawy.oblicz()} = {self.oblicz()}"


class Dziel(Wezel):

    def oblicz(self):
        return self.lewy.oblicz() - self.prawy.oblicz()

    def wypisz(self):

        napis = self.lewy.wypisz() + "\n" + self.prawy.wypisz() + "\n"
        return napis + f"{self.lewy.oblicz()} / {self.prawy.oblicz()} = {self.oblicz()}"


class Silnia(Wezel):

    def oblicz(self):
        return math.factorial(self.lewy.oblicz())

    def wypisz(self):

        napis = self.lewy.wypisz() + "\n"
        return napis + f"{self.lewy.oblicz()}! = {self.oblicz()}"


def main():

    liczba1 = Liczba(8)
    liczba2 = Liczba(3)
    liczba3 = Liczba(4)
    print(f"Liczba: {liczba1.oblicz()}")

    suma1 = Dodaj(liczba2, liczba3)
    suma2 = Dodaj(suma1, liczba1)
    print(f"Suma: {suma2.oblicz()}")

    roznica1 = Odejmij(suma2, liczba1)
    silnia1 = Silnia(roznica1)
    print(f"Silnia: {silnia1.oblicz()}")

    print("---")
    print(silnia1.wypisz())


if __name__ == "__main__":
    main()
