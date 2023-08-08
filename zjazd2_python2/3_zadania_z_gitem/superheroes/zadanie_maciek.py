from random import randint

class AngryCat:
    def __init__(self, name, superpowers):
        self.name = name
        self.superpowers = superpowers
        self.life_points = randint(1,10)

    def attack(self):
        return randint(1,10)

    def decrease_life(self, x):
        self.life_points -= x

angry_cat = AngryCat('AngryCat', ['scratching', 'biting'])