zmienna = 5
type(zmienna)
zmienna = 'napis'
type(zmienna)
zmienna = 7.5
type(zmienna)
zmienna = True
type(zmienna)

# jak konwertujemy
zmienna = int(zmienna)
zmienna = str(zmienna)
zmienna = float(zmienna)
zmienna = 'napis'
zmienna = float(zmienna)  # tu będzie błąd
zmienna = 4.5
zmienna = int(zmienna)  # tu będzie 4, bo zaokrągliło nam wartość po przecinku w dół

# podstawowe operacje na liczbach
wynik = 2 + 2
wynik = 2 * 3
wynik = (2 + 2 ** 2 * 4) / 9
wynik = (2 + 2 ** 2 * 4) / 0  # błąd - brak możliwości dzielenia przez zero
reszta = 13 % 2
reszta = 9 % 7

a = 4
b = 5
wynik = a * b

# podstawowe operacje na stringach

imie = "Jan"
nazwisko = "Kowalski"
wartosc = 400

print(imie)

# łączenie stringów
dane_osobowe = imie + nazwisko
dane_osobowe = imie + " " + nazwisko
napis = "klient {} {} posiada kapital {}.".format(imie, nazwisko, wartosc)
napis = f'klient {imie} {nazwisko} posiada kapital {wartosc}.'

# co mozemy robić na napisach
napis = "Client's details"  # zwróccie uwagę na cudzysłowia
len(napis)
napis.index("l")  # 1
napis[1]
piece_of_napis = napis[1:4]
len(piece_of_napis)
napis[1:]
napis[:-1]
napis[-4:-1]  # 'ail'
napis[::2]  # "Cin' eal"
napis.count("l")  # 2
napis = napis.upper()
napis = napis.lower()
napis = napis.title()
napis.startswith("C")  # True
napis.endswith("a")  # False
'a' in 'napis'
napis.islower()
napis.isnumeric()
'napis'.replace('a', 'o')
