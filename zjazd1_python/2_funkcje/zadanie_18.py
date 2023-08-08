# ZADANIE 18: Napisz funkcję usuwającą znaki specjalne

def usun_specjalne(napis):

    czysty_napis = list()

    for wyraz in napis.split():

        czysty_wyraz = list()

        for znak in wyraz:
            if znak.isalnum():
                czysty_wyraz.append(znak)

        if czysty_wyraz:
            czysty_napis.append("".join(czysty_wyraz))

    return " ".join(czysty_napis)


my_str = "Napis, (ze znakami !) specjalnymi ? %$\n"
print(usun_specjalne(my_str))
