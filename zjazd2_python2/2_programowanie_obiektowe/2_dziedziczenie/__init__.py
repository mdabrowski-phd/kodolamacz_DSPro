class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def grow_up(self, age):
        self.age += age
#


class Dog(Animal):
    def __init__(self, name, age, hair_color, toy):
        super().__init__(name, age)
        self.hair_color = hair_color
        self.favourite_toy = toy

    def give_voice(self):
        print("hau hau, my name is {}".format(self.name))
#


class Parrot(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color
#


dog1 = Dog('Azor', 5, 'brown', 'bone')
print(dog1.name, dog1.age)
dog1.grow_up(2)
dog1.give_voice()
print(dog1.age)

parrot1 = Parrot('Klara', 8, 'blue')
print(parrot1.name, parrot1.age, parrot1.color)
parrot1.grow_up(2)
print(parrot1.name, parrot1.age, parrot1.color)
