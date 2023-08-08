# 2. Znajdź liczby występujące zarówno w pliku numbers_1.txt jak
# i w pliku numbers_2.txt

with open('files/numbers_1.txt', 'r') as f1, open('files/numbers_2.txt', 'r') as f2:

    liczby1 = f1.readlines()
    liczby2 = f2.readlines()

liczby = [liczba.strip() for liczba in liczby1 if liczba in liczby2]
print(liczby)
