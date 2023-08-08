# ZADANIE 10: Stwórz funkcję przyjmującą string.
# Policz ile znajduje się w nim liter,
# znaków specjalnych oraz cyfr

def policz_znaki(napis):

    lit, spe, cyf = 0, 0, 0
    for znak in napis:

        if znak.isdigit():
            cyf += 1
        elif znak.isalpha():
            lit += 1
        else:
            spe += 1

    return lit, spe, cyf


input_str = "P#@yn26at^&i5ve"
litery, specjalne, cyfry = policz_znaki(input_str)

print(input_str)
print(f"Liczba liter: {litery} \nLiczba znaków specjalnych: {specjalne} \nLiczba cyfr: {cyfry}")
