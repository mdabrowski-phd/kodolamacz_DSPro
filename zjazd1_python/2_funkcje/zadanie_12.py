# ZADANIE 12: Stwórz funkcję
# która dla każdego elementu listy (inty) będzie wyświetlała
# sume elementu
# i poprzednich elementów

def suma_skumulowana(lista):

    suma = 0
    for el in lista:
        suma += el
        print(suma)


liczby = [4, -3, 6, 2, -8, 0, 1, 5]
suma_skumulowana(liczby)
