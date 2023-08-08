# ZADANIE 8: Napisz funkcje, zamieniającą literę a
#  w napisie na "X". ‘Ala’ -> XlX

def zamien_a_na_x(napis):
    return napis.replace("a", "X").replace("A", "X")


print(zamien_a_na_x("Ala"))
