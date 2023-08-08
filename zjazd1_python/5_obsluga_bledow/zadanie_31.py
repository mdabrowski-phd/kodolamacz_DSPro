# Napisz funkcję dzieląca liczby,
# z uwzględnieniem ZeroDivisionError oraz TypeError.
# Jeśli uzytkownik poda ktorąś z liczb większą od
# 100 zwróc jakiś błąd (ValueError).

def podziel(liczba1, liczba2):

    try:
        if liczba1 > 100 or liczba2 > 100:
            raise ValueError("Zbyt duże liczby!")

        return liczba1 / liczba2

    except ZeroDivisionError:
        print("Niedozwolone dzielenie przez zero!")

    except TypeError:
        print("Niepoprawne argumenty!")


dzielna = 5
dzielnik = 't'

wynik = podziel(dzielna, dzielnik)
print(f"Wynik działania: {wynik}")
