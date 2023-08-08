def sum_numbers():
    print(2 + 2)


sum_numbers
sum_numbers()


def sum_numbers(number_1, number_2):
    print(number_1 + number_2)


sum_numbers(1, 2)


def sum_numbers(number_1, number_2):
    return number_1 + number_2


number = sum_numbers(1, 2)


# dokumentacja
def calc_perc(num1, num2):
    """
    calculate percentage
    """
    return num1 * num2 / 100


# zwracanie wielu argumentów
def funkcja_wielu(num1, num2):
    return num1 + num2, num1 * num2, num1 / num2


# wartości domyslne:
def calculate_sum(arg1, arg2=100):
    return arg1 + arg2


# możemy dodać wiele niezdefiniowanych argumentów do funkcji
def super_funkcja(*args):
    for arg in args:
        print(arg)


super_funkcja('ala', 'ma', 'kota', 5)


# możemy dodać argumenty w postaci klucz wartość
def super_funkcja(**kwargs):
    for k, v in kwargs.items():
        print(k, v)


super_funkcja(imie='ala', wiek=5)
