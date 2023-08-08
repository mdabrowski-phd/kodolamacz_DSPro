def zad1(dochod):
    """
    Dla danego dochodu policz podatek na następujących zasadach:

    - gdy dochód wynosi mniej niż 85 000, to podatek wynosi 10% z dochodu;
    - jeśli dochód jest większy lub równy 85 000, ale mniejszy niż 170 000, to podatek wynosi 15% z dochodu;
    - gdy dochód jest większy lub równy 170 000, to podatek wynosi 15% ze 170 000 i 20% z dochodu
    pomniejszonego o 170 000.

    Policz podatek dla następujących dochodów: 36 000, 120 000, 240 000.
    """

    if dochod < 85_000:
        return 0.1 * dochod
    elif dochod < 170_000:
        return 0.15 * dochod
    else:
        return 0.15 * 170_000 + 0.2 * (dochod - 170_000)


def zad2(dochod):
    # Dla każdej kwoty z listy / tablicy / wektora `[50000, 10000, 200000, 75000, 1200000]`
    # oblicz podatek według schematu z poprzedniego zadania i wypisz go w postaci (bez części ułamkowej):

    # Dochód: 50000, podatek: 5000
    # Dochód: 10000, podatek: 1000

    if dochod < 85_000:
        return int(0.1 * dochod)
    elif dochod < 170_000:
        return int(0.15 * dochod)
    else:
        return int(0.15 * 170_000 + 0.2 * (dochod - 170_000))


def zad3(zakres):
    # Dla liczb z zakresu od 1 do `N` wypisz liczby, które są podzielne przez 15, 5 i 3 w następujący sposób:
    # gdy liczba jest podzielna przez 15, wypisz "Liczba `X` jest podzielna przez 15", gdzie `X` to rozpatrywana liczba.
    # Gdy liczba jest podzielna przez 5, wypisz "Liczba `X` jest podzielna przez 5".
    # Gdy liczba jest podzielna przez 3, wypisz "Liczba `X` jest podzielna przez 3".
    # Dla każdej liczby należy wypisać maksymalnie jeden napis. Przetestuj kod dla `N` = 20

    for liczba in range(1, zakres + 1):

        if liczba % 15 == 0:
            print(f"Liczba {liczba} jest podzielna przez 15.")
        elif liczba % 5 == 0:
            print(f"Liczba {liczba} jest podzielna przez 5.")
        elif liczba % 3 == 0:
            print(f"Liczba {liczba} jest podzielna przez 3.")


def zad4(a, b):
    # Dane są liczby `a` i `b`. Stwórz napis postaci `ab`. Przykładowo, dla `a = 123`, `b = 456`
    # wynikiem powinien być napis `"123456"`.
    return str(a) + str(b)


def zad5(a, b, c):
    # Napisz funkcję, która dla podanych trzech argumentów, zwraca ich maksimum, nie używając funkcji `max()`.
    # Przetestuj kod dla danych trójek: `1, 2, 3`; `4, 6, 5`; `9, 8, 7`.

    if b <= a >= c:
        return a
    elif a <= b >= c:
        return b
    else:
        return c


def zad6(napis):
    # Napisz funkcję `czy_wielka`, przyjmującą na wejściu napis. Jako wynik zwróć wartość logiczną (`True` / `False`),
    # informującą, czy podany napis zaczyna się wielką literą.
    return napis[0].isupper()


def zad7(lista):
    # Napisz funkcję, która dla danej listy / tablicy / wektora zwraca listę / tablicę / wektor, składającą się
    # tylko z elementów leżących na parzystych pozycjach.
    return [lista[i] for i in range(len(lista)) if i % 2 == 1]


def zad8(n):
    # Napisz funkcję, która dla danego `n` z zakresu od 1 do 9 zwraca wynik następującego dodawania: `n + nn + nnn`.
    # Przykładowo, dla `n = 5` zwrócimy wynik dodawania `5 + 55 + 555`.
    return n + int(str(n)+str(n)) + int(str(n)+str(n)+str(n))


def zad9(lista, x):
    # Napisz funkcję `gdzie`, która dla danej listy / tablicy / wektora `l` i liczby `x`, zwróci pozycję elementu `x`
    # w liście / tablicy / wektorze `l`.
    # W przypadku, gdy liczba wystąpi więcej niż raz w danej liście / tablicy / wektorze, zwróć pozycję
    # jej pierwszego wystąpienia. Jeśli liczba `x` nie występuje w liście / tablicy / wektorze `l`, zwróć `-1`.
    # Przetestuj kod dla `l = [6, 4, 4, 1, 5, 3, 7, 3]` i `x = 1`, `x = 2`, `x = 3`, `x = 4`.
    # Celem zadania jest implementacja rozwiązania bez wykorzystania gotowych funkcji rozwiązujących ten problem.

    for i in range(len(lista)):
        if lista[i] == x:
            return i

    return -1


def zad10(lista, x):
    # Zmodyfikuj funkcję z poprzedniego zadania, tak aby, w przypadku, gdy liczba wystąpi więcej niż raz w danej
    # liście / tablicy / wektorze, zwróć pozycję jej ostatniego wystąpienia.

    for i in range(len(lista)-1, -1, -1):
        if lista[i] == x:
            return i

    return -1


def zad11(lista):
    # Napisz funkcję, która dla danej listy / tablicy / wektora, zwraca listę zawierająca tylko liczby dodatnie.
    return [el for el in lista if el > 0]


def zad12(lista, napis):
    # Zmodyfikuj funkcję z poprzedniego zadania tak, aby funkcja przyjmowała dwa argumenty: listę / tablicę / wektor
    # oraz napis: `"dodatnie"` lub `"ujemne"`.
    # Funkcja ma zwracać listę / tablicę / wektor zawierającą elementy dodatnie lub ujemne w zależności od tego,
    # jaki napis został podany. W przypadku, gdy napis nie jest żadnym z dwóch dostępnych napisów
    # (`"dodatnie"` lub `"ujemne"`), zwróć pustą listę / tablicę / wektor.

    if napis == "dodatnie":
        return [el for el in lista if el > 0]
    elif napis == "ujemne":
        return [el for el in lista if el < 0]
    else:
        return []


def zad13(lista, napis="dodatnie"):
    # Zmodyfikuj funkcję z poprzedniego zadania tak, aby funkcja domyślnie przyjmowała napis `"dodatnie"`.

    if napis == "dodatnie":
        return [el for el in lista if el > 0]
    elif napis == "ujemne":
        return [el for el in lista if el < 0]
    else:
        return []


def main():

    print("\n---zad1---")
    dochod = 36_000  # 120_000, 240_000
    print(f"Dla dochodu {dochod} podatek wynosi {zad1(dochod)}.")

    print("\n---zad2---")
    dochody = [50_000, 10_000, 20_0000, 75_000, 1_200_000]
    for dochod in dochody:
        print(f"Dochód {dochod}, podatek: {zad2(dochod)}")

    print("\n---zad3---")
    zakres = 20
    zad3(zakres)

    print("\n---zad4---")
    a, b = 123, 456
    print(f"Złączenie {a} i {b} daje {zad4(a, b)}")

    print("\n---zad5---")
    print(f"Maksimmu z trójki (1, 2, 3) to {zad5(1, 2, 3)}")
    print(f"Maksimmu z trójki (4, 6, 5) to {zad5(4, 6, 5)}")
    print(f"Maksimmu z trójki (9, 8, 7) to {zad5(9, 8, 7)}")

    print("\n---zad6---")
    napis = "abc"
    print(zad6(napis))
    napis = "Abc"
    print(zad6(napis))

    print("\n---zad7---")
    lista = [1, 5, 6, 3, 7, 9, 4, 3, 7]
    print(lista)
    print(zad7(lista))

    print("\n---zad8---")
    n = 5
    print(f"Dla n = {n} wynik dodawania {n}+{zad4(n, n)}+{zad4(n, zad4(n, n))} to {zad8(n)}")

    print("\n---zad9---")
    lista = [6, 4, 4, 1, 5, 3, 7, 3]
    x = 1  # x = 2, x = 3, x = 4
    print(f"Element {x} znajduje się w liście {lista} na pozycji {zad9(lista, x)}")

    print("\n---zad10---")
    lista = [6, 4, 4, 1, 5, 3, 7, 3]
    x = 4  # x = 1, x = 2, x = 3
    print(f"Element {x} znajduje się w liście {lista} na pozycji {zad10(lista, x)}")

    print("\n---zad11---")
    lista = [1, 5, -6, 3, 7, -9, 4, 3, -7]
    print(lista)
    print(zad11(lista))

    print("\n---zad12---")
    lista = [1, 5, -6, 3, 0, 7, -9, 4, 3, 0, -7]
    print(lista)
    print(zad12(lista, "dodatnie"))
    print(zad12(lista, "ujemne"))

    print("\n---zad13---")
    lista = [1, 5, -6, 3, 0, 7, -9, 4, 3, 0, -7]
    print(lista)
    print(zad13(lista))
    print(zad13(lista, "ujemne"))
    print(zad13(lista, "wszystkie"))


if __name__ == "__main__":
    main()
