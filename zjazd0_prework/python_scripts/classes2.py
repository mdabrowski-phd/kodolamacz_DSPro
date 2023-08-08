import math


class LiczbaZespolona:

    def __init__(self, re, im):
        self.__re = re
        self.__im = im

    def wypisz(self):
        if self.__im < 0:
            print(f"Liczba = {self.__re}{self.__im}i")
        else:
            print(f"Liczba = {self.__re}+{self.__im}i")

    def modul(self):
        return math.sqrt(self.__re**2 + self.__im**2)

    @staticmethod
    def dodaj(z1, z2):
        return LiczbaZespolona(z1.__re + z2.__re, z1.__im + z2.__im)

    @staticmethod
    def odejmij(z1, z2):
        return LiczbaZespolona(z1.__re - z2.__re, z1.__im - z2.__im)

    @staticmethod
    def mnoz(z1, z2):
        return LiczbaZespolona(z1.__re * z2.__re - z1.__im * z2.__im,
                               z1.__re * z2.__im + z1.__im * z2.__re)


def main():

    f1 = LiczbaZespolona(2, 3)
    f2 = LiczbaZespolona(1, -2)

    f1.wypisz()
    f2.wypisz()

    print(f"Moduł = {round(f1.modul(), 2)}")

    f3 = LiczbaZespolona.dodaj(f1, f2)
    f3.wypisz()

    f4 = LiczbaZespolona.odejmij(f1, f2)
    f4.wypisz()

    f5 = LiczbaZespolona.mnoz(f1, f2)
    f5.wypisz()


if __name__ == '__main__':
    main()
