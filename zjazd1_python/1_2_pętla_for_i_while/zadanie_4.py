# ZADANIE 4: napisz program, który będzie wyświetlał pojedyncze słowa z poniższej
# listy zdań

lista_zdan = ["ala ma kota", 'jan ma psa', 'jaka to melodia']

for el in lista_zdan:
    wyrazy = el.split()
    for wyraz in wyrazy:
        print(wyraz)
