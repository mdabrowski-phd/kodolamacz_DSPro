# Z 52 elementowej talii kart, wylosuj 20 i oblicz procent 'silnych kart'
# wśrod wszystkich. Przyjmij, ze silnych kart w talii jest 16, a słabych 36

import random


def procent_silnych():

    karty = random.sample(list(range(1, 53)), 20)
    silne = 0

    for karta in karty:
        if karta <= 16:
            silne += 1

    return karty, 100 * (silne / 20)


reka, procent_silne = procent_silnych()
print(f"Na ręce {reka} jest {int(procent_silne)}% silnych kart")
