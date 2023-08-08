# Atrybuty:
# # # # name – ‘superman’
# # # # superpowers – lista supermocy np [‘ab’, ‘bc’, ‘cd’]
# # # # life_points – randomowa liczba z zakresu 1-10 - biblioteka random (random.randint)
# # # #
# https://docs.python.org/3/library/random.html#random.randint
# random.choice : https://docs.python.org/3/library/random.html#random.choice
# # #
# # # # Metody:
# # # # attack – return randomowa liczba z zakresu 1-10
# # # # decrease_life  - obniża liczbe punktów życia o podaną ilość
# # # # (x wchodzi jako parameter do funkcji: def decrease_life(self, x) )
# # #
# # # # Tworze obiekt poprzez: superman = Superman()
# import superman from zadanie_superheroes

from random import randint


class SuperHero:

    def __init__(self, name, superpowers):

        self.name = name
        self.superpowers = superpowers
        self.life_points = randint(1, 10)

    @staticmethod
    def attack():
        return randint(1, 10)

    def decrease_life(self, points):
        self.life_points -= points


superman = SuperHero("Superman", ['sila', 'szybkosc', 'latanie'])