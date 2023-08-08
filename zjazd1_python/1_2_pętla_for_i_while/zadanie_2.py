# ZADANIE 2: napisz program, który będzie pobierał od użytkownika słowa,
# i dodawał je do listy
lista = list()

while True:

    slowo = input()

    if slowo == "exit":
        break

    lista.append(slowo)

print(lista)
