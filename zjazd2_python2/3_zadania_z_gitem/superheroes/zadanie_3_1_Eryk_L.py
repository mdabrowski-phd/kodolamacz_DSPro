import random
from random import randint


class SuperHero:
    def __init__(self, name, superpowers):
        self.name = name
        self.superpowers = superpowers
        self.life_points = random.randint(1,10)

    def attack(self):
        return randint(1,10)

    def decrease_life(self, x):
        self.life_points -= x

super_herosik_komarek = SuperHero("super_herosik_komarek", ['rach', 'ciach', 'stuk'])