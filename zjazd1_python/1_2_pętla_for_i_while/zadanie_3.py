# ZADANIE 3: napisz program, który będzie dodawał 1 do każdego elementu listy,
# ale wyświetlał tylko postęp, czyli który element obecnie przetwarza. Między elementami
# powinna być sekunda "oczekiwania"
from time import sleep

# sleep(10)
lista = [10, 20, 30, 40, 50, 60]

for idx, el in enumerate(lista):

    print(f"Przetwarzam element {el}")
    lista[idx] += 1
    sleep(1)

print(lista)
