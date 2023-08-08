import math


class Ulamek:

    def __init__(self, licznik, mianownik):

        if mianownik == 0:
            raise ValueError("Mianownik ułamka musi być różny od zera!")

        self.__licznik = licznik
        self.__mianownik = mianownik
        self.__skroc__()

    def wypisz(self):

        if self.__mianownik < 0:
            print(f"{-self.__licznik}/{abs(self.__mianownik)}")
        else:
            print(f"{self.__licznik}/{self.__mianownik}")

    def __skroc__(self):

        nwd = math.gcd(self.__licznik, self.__mianownik)
        self.__licznik //= nwd
        self.__mianownik //= nwd
        return self

    @staticmethod
    def dodaj(x1, x2):
        return Ulamek(x1.__licznik * x2.__mianownik + x2.__licznik * x1.__mianownik,
                      x1.__mianownik * x2.__mianownik).__skroc__()

    @staticmethod
    def odejmij(x1, x2):
        return Ulamek(x1.__licznik * x2.__mianownik - x2.__licznik * x1.__mianownik,
                      x1.__mianownik * x2.__mianownik).__skroc__()

    @staticmethod
    def mnoz(x1, x2):
        return Ulamek(x1.__licznik * x2.__licznik,  x1.__mianownik * x2.__mianownik).__skroc__()

    @staticmethod
    def dziel(x1, x2):
        return Ulamek(x1.__licznik * x2.__mianownik, x1.__mianownik * x2.__licznik).__skroc__()


def main():

    x1 = Ulamek(-10, 12)
    x1.wypisz()

    x2 = Ulamek(6, 8)
    x2.wypisz()

    x3 = Ulamek.dodaj(x1, x2)
    x3.wypisz()

    x4 = Ulamek.odejmij(x1, x2)
    x4.wypisz()

    x5 = Ulamek.mnoz(x1, x2)
    x5.wypisz()

    x6 = Ulamek.dziel(x1, x2)
    x6.wypisz()


if __name__ == '__main__':
    main()
