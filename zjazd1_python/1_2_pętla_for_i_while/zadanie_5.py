# ZADANIE 5 : dla poniższych list stwórz listę krotek,
# której pierwszy element
# stanowi iloraz wysokości przez liczbę pięter,
# drugi element to sama nazwa kraju
# z listy 'miejca', a trzeci element to nazwa budynku:
wysokosci = [829, 632, 601, 599.3, 554.5]
liczba_pieter = [163, 128, 120, 115, 123]
miejsca = ['Dubaj, Zjednoczone Emiraty Arabskie', 'Szanghaj, Chiny',
           'Mekka, Arabia Saudyjska', 'Shenzhen, Chiny', 'Seul, Korea Południowa']
nazwy = ['Burj Khalifa', 'Shanghai Tower', 'Abradż al-Bajt', 'Ping An Finance Centern',
         'Lotte World Tower']

lista = list()

for wys, pietro, miejsce, nazwa in zip(wysokosci, liczba_pieter, miejsca, nazwy):
    lista.append((round(wys / pietro, 2), miejsce.split(", ")[1], nazwa))

print(lista)
