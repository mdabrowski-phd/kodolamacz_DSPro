# Zadanie 15: Stwórz funkcję liczącą ile cyfr jest
# w podanej liczbie

def ile_cyfr(liczba):
    return len(str(liczba))


liczba = 657_235
print(f"Liczba cyf w {liczba} to {ile_cyfr(liczba)}")
