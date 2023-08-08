# ZADANIE 4 : Stwórz listę liczb od 1 do 20. Wybierz z
# niej elementy parzyste, jednak nie bierz 10 pod uwagę.
# Nie wypisuj liczb większych niż 13

lista = list(range(1, 21))

parzyste = [el for el in lista if el % 2 == 0 and el != 10]

print(lista)
print(parzyste)

for el in parzyste:

    if el > 13:
        continue

    print(el)
