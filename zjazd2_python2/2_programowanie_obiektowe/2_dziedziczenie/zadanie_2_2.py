# 4. Utwórz klasę Person z atrybutami: imię i wiek oraz metodą, która wyświetla nazwę i wiek obiektu
# Utwórz klasę Student, która dziedziczy z klasy osoby oraz ma dodatkowy atrybut "uczelnia"
# Utwórz metodę, która wyświetla nazwę, wiek i uczelnię obiektu utworzonego za pośrednictwem klasy Student.

class Person:

    def __init__(self, imie, wiek):

        self.imie = imie
        self.wiek = wiek

    def wyswietl(self):
        print(f"Imię: {self.imie}, wiek: {self.wiek}")


class Student(Person):

    def __init__(self, imie, wiek, uczelnia):

        super().__init__(imie, wiek)
        self.uczelnia = uczelnia

    def wyswietl(self):

        super().wyswietl()
        print(f"Uczelnia: {self.uczelnia}")


osoba1 = Person("Michał", 32)
osoba1.wyswietl()

osoba2 = Student("Asia", 23, "UW")
osoba2.wyswietl()
