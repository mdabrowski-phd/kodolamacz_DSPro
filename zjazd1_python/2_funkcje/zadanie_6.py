# ZADANIE 6: Napisz funkcje przyjmującą dwa argumenty
# typu int.
# Jeśli ich iloczyn jest większy od 1000, zwróć ich sume.

def suma_warunkowa(liczba1, liczba2):
    if liczba1 * liczba2 > 1000:
        return liczba1 + liczba2


suma = suma_warunkowa(30, 45)
print(suma)
