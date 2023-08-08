# Napisz funkcję , która będzie zwracać sume i
# iloczyn wszystkich podanych argumentów

def suma_iloczyn(*args):

    su, il = 0, 1

    for liczba in args:

        su += liczba
        il *= liczba

    return su, il


suma, iloczyn = suma_iloczyn(1, 2, 3, 4, 5)
print(f"Suma: {suma}, iloczyn: {iloczyn}")
