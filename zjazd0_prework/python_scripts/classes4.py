import math
from abc import ABC, abstractmethod


class Figura(ABC):

    @abstractmethod
    def pole(self):
        pass

    @abstractmethod
    def obwod(self):
        pass

    def przedstaw_sie(self):
        print(f"Jestem {self.nazwa_figury()}, mam pole {self.pole()} oraz obwód {self.obwod()}")

    @abstractmethod
    def nazwa_figury(self):
        pass


class Kolo(Figura):

    def __init__(self, r):
        self.__r = r

    def pole(self):
        return round(math.pi * self.__r ** 2, 2)

    def obwod(self):
        return round(2 * math.pi * self.__r, 2)

    def nazwa_figury(self):
        return "koło"


class Kwadrat(Figura):

    def __init__(self, a):
        self._a = a

    def pole(self):
        return round(self._a ** 2, 2)

    def obwod(self):
        return round(4 * self._a, 2)

    def nazwa_figury(self):
        return "kwadrat"


class Prostokat(Kwadrat):

    def __init__(self, a, b):
        super().__init__(a)
        self._b = b

    def pole(self):
        return round(self._a * self._b, 2)

    def obwod(self):
        return round(2 * (self._a + self._b), 2)

    def nazwa_figury(self):
        return "prostokąt"


class Trojkat(Figura):

    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    def pole(self):
        p = self.obwod() / 2

        return round(math.sqrt(p * (p - self.__a) * (p - self.__b) * (p - self.__c)), 2)

    def obwod(self):
        return round(self.__a + self.__b + self.__c, 2)

    def nazwa_figury(self):
        return "trójkąt"


def policz_sume_pol_obwodow(figury):

    suma_pol, suma_obwodow = 0, 0
    for figura in figury:
        suma_pol += figura.pole()
        suma_obwodow += figura.obwod()

    return suma_pol, suma_obwodow


def main():

    kolo = Kolo(5)
    kolo.przedstaw_sie()

    kwadrat = Kwadrat(3)
    kwadrat.przedstaw_sie()

    prostokat = Prostokat(2, 5)
    prostokat.przedstaw_sie()

    trojkat = Trojkat(3, 4, 5)
    trojkat.przedstaw_sie()

    print(f"Suma pól i obwodów wszystkich figur: {policz_sume_pol_obwodow([kolo, kwadrat, prostokat, trojkat])}")


if __name__ == "__main__":
    main()
