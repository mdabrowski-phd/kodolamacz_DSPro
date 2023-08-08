# todo
# W pliku 'pytest.ini' znajduje się kilka sekcji, a każda sekcja zaczyna się od wyrażenia
# w nawiasach kwadratowych []. Wewnątrz każdej sekcji znajdują się pary klucz-wartość
# z opcjonalnymi spacjami koło znaku "=". Klucze mogą zawierać litery, numery, podkreślniki
# (tzw. podłoga "_") lub myślniki. Dodatkowo w pliku mogą znajdować się puste linie oraz
# linie komentarzy, rozpoczynające się od "#". Przekształć plik 'pytest.ini' do poniższej formy:
# $VAR1 = { 'earth' => { 'base' => 'London', 'ship' => 'x-wing' },
# 'alpha' => { 'base' => 'moon', 'ship' => 'alpha 3' } }

import re


kategoria_regex = re.compile(r'\[.*]')
klucz_regex = re.compile(r'.+=')
wartosc_regex = re.compile(r'=.+')

komentarz_regex = re.compile(r'#+')

dobre_linie = list()

with open("data/pytest.ini", "r") as f:

    linia = f.readline()
    while linia:

        if not re.search(komentarz_regex, linia):  # ignorowanie linii komentarza, jeżeli równość w komentarzu

            if re.search(kategoria_regex, linia):
                dobre_linie.append(re.search(kategoria_regex, linia).group()[1:-1])

            if re.search(klucz_regex, linia):
                dobre_linie.append(re.search(klucz_regex, linia).group()[:-1].strip())

            if re.search(wartosc_regex, linia):
                dobre_linie.append(re.search(wartosc_regex, linia).group()[1:].strip())

        linia = f.readline()

dict_kategorie = dict()

for i in range(0, len(dobre_linie), 5):
    dict_kategorie[dobre_linie[i]] = {dobre_linie[i+1]: dobre_linie[i+2],
                                      dobre_linie[i+3]: dobre_linie[i+4]}

print(f"$VAR1 = {re.sub(r':', r' =>', str(dict_kategorie))}")
