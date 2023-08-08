# bieda-poker: Talia kart zawiera karty w kolorach: pik, kier, karo, trefl
# w zakresie od 1 do 14. Napisz funkcje, która przyjmie liczbe graczy,
# potasuje talie kart, odrzuci tyle, aby każdy gracz mial po równo
# a nastepnie rozda karty (kazdy gracz dostaje co n-tą karte).
# Nastepnie policz, który gracz / gracze otrzymał największą liczbe kart
# tego samego koloru.

import random
import itertools

KARTY = list(itertools.product(list(range(1, 14)), ['pik', 'kier', 'karo', 'trefl']))


def rozdaj(l_graczy):

    random.shuffle(KARTY)

    karty_na_gracza = len(KARTY) // l_graczy
    talia = KARTY[0: l_graczy * karty_na_gracza]

    karty_graczy = [talia[i * karty_na_gracza: (i+1) * karty_na_gracza] for i in range(l_graczy)]

    return karty_graczy


def podlicz_karty(karty):

    max_kolor = list()

    for gracz, karty_gracza in enumerate(karty):
        print(f"Karty gracza {gracz + 1}: {karty_gracza}")

        karty_gracza_dict = dict()
        for karta in karty_gracza:
            karty_gracza_dict[karta[1]] = karty_gracza_dict.get(karta[1], 0) + 1

        print(f"Pogrupowane kolorami: {karty_gracza_dict}\n")
        max_kolor.append(max(karty_gracza_dict.values()))

    return max_kolor


def wypisz_max(karty_kolor):

    max_kolor = max(karty_kolor)
    for i, el in enumerate(karty_kolor):
        if el >= max_kolor:
            print(f"Gracz {i+1} ma aż {el} kart w jednym kolorze")


liczba_graczy = 5
rozdane_karty = rozdaj(liczba_graczy)
wypisz_max(podlicz_karty(rozdane_karty))
