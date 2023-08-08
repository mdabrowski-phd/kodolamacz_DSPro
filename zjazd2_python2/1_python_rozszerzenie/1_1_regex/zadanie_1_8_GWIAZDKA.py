# 8. Stwórz słownik danych osobowych z poniższego stringa
# Przyjmijmy, że zawsze w naszym zbiorze na początku występuje imie i nazwisko
# oraz że poniższy string reprezentuje sposob zapisu naszych danych

import re


string_z_danymi = 'Karol Kowalski, ul.Prosta 5/10, 675-835-578, 04-445'

dane_osobowe = {"imie i nazwisko": re.search(r'\S+\s\S+\b', string_z_danymi).group(),
                "ulica": re.search(r'(?<=ul\.)\S+\s\S+\b', string_z_danymi).group(),
                "telefon": re.search(r'\d{3}-\d{3}-\d{3}', string_z_danymi).group(),
                "kod pocztowy": re.search(r'\d{2}-\d{3}', string_z_danymi).group()}

# dane_osobowe = {
#  'imie i nazwisko': re.search(r'^\w+ \w+,', string_z_danymi).group()[:-1],
#  'adres': re.search(r'ul\..+?,', string_z_danymi).group()[:-1],
#  'numer tel': re.search(r'\d{3}-\d{3}-\d{3}', string_z_danymi).group(),
#  'kod': re.search(r'\d{2}-\d{3}', string_z_danymi).group()
# }

print(dane_osobowe)
