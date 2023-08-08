# # REGEX - wyrażenia regularne
import re

# importowanie modulow
# from tests import test_count
# from tests.test_count import sum_num

# test_count.sum_num(1,2)
# sum_num(1,)


print('\tTekst\n')
print(r'\tTekst')

# Funkcja match() zwraca znaleziony napis, jeśli od początku pasuje do patternu. W innym przypadku zwróci None.
pattern = r"napis"
sequence = "napis tu jest napisany"
print(re.match(pattern, sequence))
#
#
pattern = r"napis"
sequence = "napis tu jest napisany"
print(re.match(pattern, sequence).group())

pattern = r"78"
sequence = "napis tu jest napisany"
if_match = re.match(pattern, sequence)
if if_match:
    print(re.match(pattern, sequence).group())
#
#
# # search() w przeciwieństwie do match szuka patternu w całym stringu
#
moj_regex = re.compile(r'ma')
print(re.search(moj_regex, 'Ala ma kota'))
print(re.search(moj_regex, 'mama ma kota'))

pattern = r"napis"
sequence = "To taki napis"
print(re.search(pattern, sequence).group())
#
#
# # Kropka oznacza dowolny znak, oprócz znaku nowej linii
#
print(re.search(r'N.p.s', 'Napis'))
print(re.search(r'N.p.s', 'ala ma kota Nop5s'))

# ^ oznacza początek napisu
print(re.search(r'^Na.', 'Napis ala ma kota').group())
print(re.search(r'^Na.', 'Na? jj Nal').group())
#
# # $ oznacza koniec napisu
#
print(re.search(r'Na.$', 'Napis'))
print(re.search(r'Na.$', 'isNap'))

# # \* powtarza ostatni znak zero lub wiele razy
print(re.search(r'^Na.*', 'Napis').group())
print(re.search(r'^Na.*', 'Na').group())
print(re.search(r'^Na.*', 'Napis ma kota').group())

#
# # \+ powtarza ostatni znak przynajmniej raz
#
print(re.search(r'Na.*', 'Na'))
print(re.search(r'Na.+', 'Na'))
print(re.search(r'Na.+', 'Napppp222????!!%%%'))

#
# # Czasem możemy chcieć zawęzić zakres np w przypadku szukania takiego wzorca:
# # (.*) w takim stringu
# #
# # "(a) b (c)"
# #
# #  zostanie znalezione
# #
# #  "(a) b (c)"
# #
# #  zamiast jedynie
# #
# #  (a)
# #
# # ? w skrócie ogranicza zakres do jak najmniejszego
#
print(re.search(r'Na*?', 'Naaaaa'))  # zero lub wiele
print(re.search(r'Na*', 'Naaaaa'))
print('\n')
print(re.search(r'a+?', 'Naaaaa'))  # mimum jeden
print(re.search(r'a+', 'Naaaaa'))
#
# # Jeśli natomiast chcemy wykorzystać poznane powyżej symbole dla większej grupy znaków to możemy zgrupować je w
# # [ ] i następnie użyć któregoś z symbolu lub symboli
#
print(re.search(r'[lj*?]+', '?h*fjalafelhh?*'))
print(re.search(r'[lj*?]+', '?jllj*h*fjalafelhh?*'))
print(re.search(r'[abc]', 'falabac'))
print(re.search(r'[alh]+', 'lahla'))

#
# # Istnieją też skróty, które pozwalają nam wyszukiwać grupy znaków szybciej
# #
# #     * \d - cyfry == [0-9]
# #     * \D - nie cyfry
# #     * \s - spacje, taby, nowe linie itp
# #     * \S - stringi, włączając w to znaki specjalne oraz cyfry
# #     * \w - słowa + cyfry, czyli j.w. bez znaków specjalnych [a-zA-Z0-9_]
# #     * \W - zaprzeczenie w.w.
# #     * \b - samodzielne slowo
# https://docs.python.org/3/library/re.html#regular-expression-syntax


#
# # %%
#
print(re.search(r'\s+', 'Warszawa        to piekne miasto'))
#
# # %%
#
print(re.search(r'\S+', 'Warszawa to piekne miasto '))
#
# # %%
#
print(re.search(r'\S+', 'Wars334&zawa to piekne miasto'))
#
# # %%
#
print(re.search(r'\w+', 'Warszawa to piekne miasto'))
#
# # %%
#
print(re.search(r'\W+', 'Warszawa++?*)%^&)234??? to piekne miasto'))
#
# # %%
#
print(re.search(r'\d+', 'Warszawa++?*)%^&)23434??? to piekne miasto'))
print(re.search(r'\d+?', 'Warszawa++?*)%^&)234??? to piekne miasto'))
#
# # %%
#
print(re.search(r'\D+', 'Warszawa++?*)%^&)234576??? to piekne miasto'))
#
# # {m} oznacza ile powtórzeń danego znaku chcemy
#
print(re.search(r'\d{2}-\d{3}', '02-081').group())
print(re.search(r'\d{2}-\d{3}', '022-081').group())
#
# # {m,n} określa dokładny zakres ilości powtórzeń

print(re.search(r'\d{3,4}-\d{3}', '0289-081'))
print(re.search(r'\d{4,}-\d{3}', '02289-081'))
# # #
# # A co jeśli chcemy znaleźć napisy z ukośnikami, kropkami lub plusami?
# Może posłużyć się znakiem 'ucieczki': \
#

print(re.search(r'\d+\+\d+', '22+2'))
print(re.search(r'\d+[+]\d+', '22+2'))
print(re.search(r'\d+\*\d+', '2*2'))
print(re.search(r'\d+\+\d+', '+2'))
#
# # W nawiasach kwadratowych możemy określać również zakres np od a do z:
# [a-z] oraz od 0 do 9 [0-9],
# # czyli w praktyce wszystkie litery lub cyfry
#
print(re.search(r'[a-z]+', 'falafel'))
print(re.search(r'[a-z*]+', 'fala**fel'))
#
print(re.search(r'\d', '9573528'))
print(re.search(r'[0-8]+', '9573528'))
#
print(re.search(r'[0-9]+[a-z]+', '9573528hafdyusk94635'))
print(re.search(r'[0-9][a-z]+', '9573528hafdyusk94635'))

#
# # Znaki specjalne tracą swoje specjalne znaczenie w nawiasach kwadratowych
# np [(+*)] oznacza znajdź mi otwarcie okrągłego nawiasu, plus,
# gwiazdkę lub zamknięcie okrągłego nawiasu
#
print(re.search(r'[(+*)]', 'ababa + ababa'))
print(re.search(r'[(+*)]+', 'ababa ((++ ababa '))
#
# # W nawiasach kwadratowych zastosowanie ^ oznacza znak wykluczenia,
# a więc będziemy szukać wszystkiego poza tym znakiem
#
print(re.search(r'[^51]+jajko[^5]+', '551234jajko67589'))
#
# # %%
#
print(re.search(r'Warszawa|Krakow', 'Krakow to piekne miasto'))
#
# # Aby znaleźć wszystkie dopasowania stosujemy findall() zamiast search()
#
print(re.findall(r'\w+', 'Warszawa to piekne miasto 234'))
#
# # Możemy też wykorzystać wyrażenia regularne do zamiany na inny string dzięki wykorzystaniu sub()
# # %%
#

print('ala ma kotra'.replace("kotra", "kota"))
print(re.sub(r'\w+', 'zmieniony', 'Warszawa to piekne miasto &&??'))


#
#
# # https: // regex101.com /


# NIEZALEŻNE SLOWA
# print(re.findall(r' ma ', 'mama ma kota i maluje.ma kota'))
# print(re.findall(r' ma', 'ona to ma.'))
# print(re.findall(r'ma ', 'ma ona to'))
# # to co ponizej == powyzej:
# print(re.findall(r'\bma\b', 'mama ma kota i maluje.ma kota'))
# print(re.findall(r'\bma\b', 'ona to ma.'))
# print(re.findall(r'\bma\b', 'ma ona to'))


# szukamy paternu z początkiem ale chcemy wyswietlic bez poczatku
# ?<=
# ?<!
print(re.search('(?<=abc)def', 'abcdef').group())
# ==
print(re.search('abcdef', 'abcdef').group()[3:])
print(re.findall('(?<!\d)[a-z]+', 'abcdef 567abc'))

# print(re.search('DEF', 'abcdef', flags=re.IGNORECASE).group())

