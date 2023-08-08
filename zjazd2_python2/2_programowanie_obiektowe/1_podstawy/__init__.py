# KLASY
class Dog:
    def __init__(self):
        self.name = 'Azor'
        self.age = 5
# #


dog1 = Dog()  # funkcja()
print(dog1.name, dog1.age)


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age


dog1 = Dog("Azor", 6)
# #
print(dog1.name, dog1.age+1)
dog1.name = 'azor2'
print(dog1.name)

#


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def give_voice(self):
        print("hau hau, my name is {}".format(self.name))

    def add_age(self, numb):
        self.age += numb
#


dog1 = Dog("Azor", 5)
dog1.give_voice()
dog1.add_age(1)
print(dog1.age)

#
dog1.age = 4
print(dog1.age)
#
dog2 = Dog("Burek", 6)
print(dog2.name, dog2.age)
#
dog2.give_voice()


class Dog:
    def __init__(self, name, age, animal_type='dog'):
        self.name = name
        self.age = age
        self.animal_type = animal_type
#


dog1 = Dog("Burek", 6)
print(dog1.name, dog1.age, dog1.animal_type)
#
dog1 = Dog("Burek", 6, 'cat')
print(dog1.name, dog1.age, dog1.animal_type)
#
dog1.animal_type = 'dog'
print(dog1.animal_type)
#
dog2 = Dog(5, "Azor")
print(dog2.name, dog2.age, dog2.animal_type)


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def count_age(self, years):
        self.age = years + self.age
        print("jestem {}, za {} lat bede mial {} lat".format(self.name, years, self.age))

    def set_age(self, num):
        self.age += num
#


dog1 = Dog("Azor", 5)
dog1.count_age(5)
