# Mając zbiór danych z zadania 5, stwórz 2_funkcje, które:
wysokosci = [829, 632, 601, 599.3, 554.5]
liczba_pieter = [163, 128, 120, 115, 123]
miejsca = ['Dubaj, Zjednoczone Emiraty Arabskie', 'Szanghaj, Chiny', 'Mekka, Arabia Saudyjska', 'Shenzhen, Chiny',
           'Seul, Korea Południowa']
nazwy = ['Burj Khalifa', 'Shanghai Tower', 'Abradż al-Bajt', 'Ping An Finance Centern', 'Lotte World Tower']


def create_dict():
    """
    stworzy słownik nazwa: (wysokosc, liczba_pieter), np {'Burj Khalifa':(829, 163)}
    """

    sl = dict()

    for nazwa, wys, pietro in zip(nazwy, wysokosci, liczba_pieter):
        sl[nazwa] = (wys, pietro)

    return sl


def add_record(sl, nazwa, params):
    """
    pozwoli dodawac rekordy do slownika (user podaje wszystkie wartosci)
    """

    sl[nazwa] = params
    return sl


def remove_record(sl, nazwa):
    """
    bedzie usuwac rekordy ze słownika po kluczu
    """

    if nazwa in sl:
        del sl[nazwa]

    return sl


def check_record(sl, params):
    """
    bedzie zwracac uzytkownikowi, czy dany klucz znajduje sie w słowniku
    i czy posiada podana przez uzytkownika wysokosc, np. ('Burj Khalifa', 600) -> False
    """
    # params = (nazwa, wysokosc)
    return params[0] in sl and params[1] == sl[params[0]][0]


def srednia_pieter(sl):
    """
    policzy srednią ilosc pieter wszystkich budynkow w slowniku
    """

    suma = 0
    for el in slownik.values():
        suma += el[1]

    return suma / len(sl)


print("\n---tworzenie slownika")
slownik = create_dict()
print(slownik)

print("\n---dodanie elementu")
add_record(slownik, 'aaa', (20, 40))
print(slownik)

print("\n---sprawdzenie elementu")
print(check_record(slownik, ('Burj Khalifa', 829)))
print(check_record(slownik, ('aaa', 25)))
print(check_record(slownik, ('aaa', 20)))

print("\n---usuniecie elementu")
remove_record(slownik, 'aaa')
print(slownik)

print("\n---srednia liczba pieter")
print(f"Srednia liczba pięter: {srednia_pieter(slownik)}")
