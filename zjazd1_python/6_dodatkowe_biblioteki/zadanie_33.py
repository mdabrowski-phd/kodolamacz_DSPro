# Stwórz funkcje liczyć średnią z listy 10000 wylosowanych liczb w zakresie 1-100

import random
from statistics import mean


def srednia_z_proby():
    return mean(random.choices(list(range(1, 101)), k=1000))


print(srednia_z_proby())
