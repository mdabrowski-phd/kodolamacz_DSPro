
"""
Kalkulator: w trzech liniach podajemy kolejno pierwszą liczbę, operator działania (+, -, *, /, //, %) oraz drugą liczbę.
Program wykonuje się przynajmniej jeden raz, nie jest sprawdzana poprawność podania argumentów przez użytkownika.
Program działa w pętli, która jest kontynuowana w przypadku wpisania znaku t, a przerywana przy podaniu znaku p.
"""


def podaj_liczbe():

    while True:

        try:
            liczba = float(input("Podaj liczbę: "))
            break
        except ValueError:
            print("Podany napis nie jest liczbą!")

    return liczba


def main():

    while True:

        pierwsza_liczba = podaj_liczbe()
        operator_dzialania = input("Podaj operator działania: ")
        druga_liczba = podaj_liczbe()

        try:
            if operator_dzialania == "+":
                wynik = pierwsza_liczba + druga_liczba

            elif operator_dzialania == "-":
                wynik = pierwsza_liczba - druga_liczba

            elif operator_dzialania == "*":
                wynik = pierwsza_liczba * druga_liczba

            elif operator_dzialania == "/":
                wynik = pierwsza_liczba / druga_liczba

            elif operator_dzialania == "//":
                wynik = pierwsza_liczba // druga_liczba

            elif operator_dzialania == "%":
                wynik = pierwsza_liczba % druga_liczba

            else:
                print("Niepoprawne działanie!")
                break

            print(f"Wynik działania: {round(wynik, 2)}")

        except ZeroDivisionError:
            print("Niedozwolone dzielenie przez zero!")

        decyzja = input("Czy chcesz kontynuować (t/n)?: ")
        if decyzja == "n":
            break


if __name__ == "__main__":
    main()
