# listy
lista = []
lista = list()
lista.append(1)
lista.append('dwa')
lista.append([1, 2, 3])
lista.insert(0, 'dodany')
lista.extend([4, 5, 6])
del lista[0]
lista.remove(1)

lista[0]
lista[1]
lista[10]  # tu error - nie ma takiego elementu

tupla = (1, 2, 3)
tupla[0]
tupla[0] = 10  # error
tupla.append(3)  # error
del tupla[0]  # error

lista[1:3]
lista[-1]
tupla[-1]
tupla[0:2]

# przydatne operacje
lista = [1, 1, 1, 1, 2, 3, 4, 4, 4]
lista_bez_powtorzen = set(lista)
lista = [6, 7, 4, 3, 7]
lista.sort()
','.join(lista)
"ala ma kota".split(' ')
