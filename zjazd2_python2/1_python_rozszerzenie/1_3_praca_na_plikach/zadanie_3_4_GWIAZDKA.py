# # 4. Napisz program podający datę urodzin osób, których nazwiska znajdują się w pliku
# 'birthdays.json'.
# # Program powinien pobierać nazwisko od użytkownika (można to zrobić funkcją 'input').
# # Zaprogramuj również możliwość podania imienia,
# # które nie istnieje na liście oraz możliwość zakończenia programu przez użytkownika.
# print('wpisz imie:')
# name = input()
# print('twoje imie to:', name)

import json


with open("files/birthdays.json", "r") as f:
    dict_birth = json.load(f)

print(dict_birth)
name = input('wpisz imie lub QUIT, aby zakończyć: ')

while name != "QUIT":

    print(dict_birth.get(name, "Podanej osoby nie ma w słowniku!"))
    name = input('wpisz imie lub QUIT, aby zakończyć: ')
