# ZADANIE 9: Napisz funkcje, zamieniającą pierwszą
# literę a w napisie na "X".
# Ala -> Xla

def zamien_pierwsza_na_x(napis):

    for znak in napis:
        if znak == "a" or znak == "A":
            return napis.replace(znak, "X", 1)

    return napis


print(zamien_pierwsza_na_x("Ala"))
