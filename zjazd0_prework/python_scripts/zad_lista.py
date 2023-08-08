def czy_dodatnia(lista):

    for element in lista:
        if element <= 0:
            return False

    return True


def srednia(lista):

    suma = 0
    for element in lista:
        suma += element

    return suma/len(lista)


def skumulowana_suma(lista):

    skumulowana = []  # skumulowana = [None] * len(lista)
    suma = 0
    for element in lista:  # index, element in enumerate(lista) ==> element == lista[index]
        suma += element
        skumulowana.append(suma)

    return skumulowana


def suma_list(lista1, lista2):

    lista = []
    for el1, el2 in zip(lista1, lista2):
        lista.append(el1 + el2)

    return lista


def main():

    l1 = [1, 2, 4, 8, 16, 32]
    l2 = [1, 2, -4, 8, 16, -32]

    print(czy_dodatnia(l2))
    print(srednia(l1))
    print(skumulowana_suma(l1))
    print(suma_list(l1, l2))


if __name__ == "__main__":
    main()
