# list comprehension
a = [x for x in range(10)]
a = [x * 2 for x in range(10)]

a = [x * 2 for x in range(10) if x % 2 == 0]
a = [x * 2 if x % 2 == 0 else x for x in range(10)]

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

# działa enumerate, zip i łączenie warunków
a = [x + y for x, y in zip(lista1, lista2)]
a = [x for x in range(10) if (x % 3 == 0 and x % 2 == 0)]

# lambda
# pozwala stworzyć anonimową funkcję z wyrażenia
funkcja_lambda = lambda x, y: x + y


# jest rownowazne
def funkcja_lambda(x, y):
    return x + y
