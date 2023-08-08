# ZADANIE 1: Z powstałego listy słownikow wybierz
# liczbę 2,
# będącą częścią listy, która jest wartością klucza 123
s1 = {'a': 2, (1, 2): 'wartosc'}
s2 = {123: [1, 2, 3]}
lista_slownikow = [s1, s2]

print(lista_slownikow[1][123][1])
