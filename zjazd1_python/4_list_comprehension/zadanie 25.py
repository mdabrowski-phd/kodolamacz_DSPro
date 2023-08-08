# stworz funkcje sumująca wszystkie argumenty,
# które są podzielne przez 3, ale mniejsze od 20 w
# poniższej liście

def oblicz(lista):
    return sum([el for el in lista if (el % 3 == 0 and el < 20)])


liczby = [22, 36, 3, 9, 5, 6, 66]
print(oblicz(liczby))
