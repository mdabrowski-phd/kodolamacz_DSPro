# operatory logiczne:
# a > b
# a == b
# a != b

imie = 'Jan'
nazwisko = 'Kowalski'
imie == 'Jan' and nazwisko == 'Kowalski'
imie == 'jan' or nazwisko == 'Kowalski'
# lub
(imie == 'jan') & (nazwisko == 'Kowalski')
(imie == 'jan') | (nazwisko == 'Kowalski')
if imie == 'jan' or nazwisko == 'Kowalski':
    print('cokolwiek jest poprawne')
if (a > b) and b == 5:
    print('wszystkie warunki spelnione')

kwota = 100

if kwota < 100:  # wyrażenie jest prawdziwe
    print('kwota poniżej 100')
elif kwota > 100:  # poprzednie wyrazenie jest falszywe, ale to prawdziwe
    print('kwota powyzej 100')
else:  # jesli zadne z powyzszych nie jest prawdziwe
    print('kwota ==100')

# można też sprawdzać, czy dany obiekt nie jest pusty
if '':
    print('True')
else:
    print('false')

# to samo z zerem lub false
# słowo not zmienia true na false

if not '':
    print('True')
else:
    print('false')