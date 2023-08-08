# napisz formułe, która z dwóch list wybierze
# element większy:

print(max([1, 2, 3]))
print(sum([1, 2, 3]))
lista1 = [1, 2, 3]
lista2 = [4, 5, 1]
# => [4,5,3]

wynik = [max(x, y) for x, y in zip(lista1, lista2)]
print(wynik)
