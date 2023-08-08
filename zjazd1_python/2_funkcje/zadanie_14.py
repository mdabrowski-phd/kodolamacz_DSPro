# Zadanie 14: Napisz kalkulator (suma, odejmowanie, mnożenie, dzielenie)
# dla dwóch liczb, sprawdź, czy użytkownik podaje odpowiednie typy danych
# i czy nie chce dzielić przez zero
# mn = mnozenie
# dz = dzielenie
# od - odejmowanie
# do - dodawania

def podaj_liczbe():

    while True:

        try:
            liczba = float(input("Podaj liczbę: "))
            break
        except ValueError:
            print("Podany napis nie jest liczbą!")

    return liczba


def kalkulator(liczba1, liczba2, dzialanie):

    try:
        if dzialanie == "+":
            return liczba1 + liczba2

        elif dzialanie == "-":
            return liczba1 - liczba2

        elif dzialanie == "*":
            return liczba1 * liczba2

        elif dzialanie == "/":
            return liczba1 / liczba2

        else:
            print("Niepoprawne działanie!")
            return None

    except ZeroDivisionError:
        print("Niedozwolone dzielenie przez zero!")
        return None


while True:

    pierwsza_liczba = podaj_liczbe()
    operator_dzialania = input("Podaj operator działania: ")
    druga_liczba = podaj_liczbe()

    wynik = kalkulator(pierwsza_liczba, druga_liczba, operator_dzialania)
    if wynik is not None:
        print(f"Wynik działania: {round(wynik, 2)}")

    decyzja = input("Czy chcesz kontynuować (t/n)?: ")
    if decyzja == "n":
        break
