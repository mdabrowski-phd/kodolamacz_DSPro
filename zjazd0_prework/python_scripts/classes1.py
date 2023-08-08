import math


class FunkcjaKwadratowa:

    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    def wypisz(self):
        print(f"f(x) = {self.__a}x^2 + {self.__b}x + {self.__c}")

    def oblicz(self, x):
        return self.__a * x**2 + self.__b * x + self.__c

    def rozwiaz(self):

        if self.__a == 0 and self.__b == 0:
            if self.__c == 0:
                return -float("inf"), float("inf")
            else:
                return float("nan"), float("nan")

        elif self.__a == 0:
            return round(-self.__c/self.__b, 2), round(-self.__c/self.__b, 2)

        else:
            delta = self.__b**2 - 4 * self.__a * self.__c
            if delta < 0:
                return float("nan"), float("nan")
            elif delta == 0:
                return round(-self.__b/(2 * self.__a), 2), round(-self.__b/(2 * self.__a), 2)
            else:
                return round((-self.__b - math.sqrt(delta))/(2 * self.__a), 2),\
                    round((-self.__b + math.sqrt(delta))/(2 * self.__a), 2)


def main():

    f1 = FunkcjaKwadratowa(0, -3, 2)
    f1.wypisz()
    print(f"f1(5) = {f1.oblicz(5)}")
    print(f"Miejsca zerowe: {f1.rozwiaz()}")


if __name__ == '__main__':
    main()
