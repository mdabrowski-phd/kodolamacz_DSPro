# # 1. Oblicz ile razy występuje każde imie w pliku 'names.txt' oraz wyświetl na ekranie

from collections import Counter


with open('files/names.txt', 'r') as f:
    imiona = f.read().splitlines()  # f.readlines() pozostawia znaki końca wiersza '\n'

counts = Counter(imiona)
print(counts)
