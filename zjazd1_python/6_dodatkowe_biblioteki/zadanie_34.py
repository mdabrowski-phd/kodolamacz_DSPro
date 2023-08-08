# STWORZ FUNKCJE LOSUJĄCĄ od 1 do 6 tak długo aż nie wylosuje 6.
# Jesli jej się uda, niech zwróci uzytkownikowi ile razy próbowała

import random


def losuj6():

    proby = 1
    wynik = random.randint(1, 6)

    while wynik != 6:

        wynik = random.randint(1, 6)
        proby += 1

    return proby


print(f"Losowanie szóstki odbyło się {losuj6()} razy")
