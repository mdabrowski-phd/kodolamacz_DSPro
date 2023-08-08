kontakty = {}
kontakty["Jan"] = 938477566
kontakty["Jacek"] = 938377264
kontakty["Janusz"] = 947662781

kontakty = {
    "Jan": 938477566,
    "Jacek": 938377264,
    "Janusz": 947662781
}

# pobieranie elementów
kontakty['Janusz']
kontakty.get('Janusz')
# indeksowanie tylko po kluczu a nie po indeksie
kontakty[0]
# kluczem w słowniku nie może być lista bo jest mutowalna

# nie bedzie po kolei:
for imie, numer in kontakty.items():
    print(imie, numer)

for imie in kontakty:
    print(imie, kontakty[imie])

for imie in kontakty.keys():
    print(imie)

for numer in kontakty.values():
    print(numer)

# usuwanie
del kontakty["Jan"]

# przeszukiwanie
'Julita' in kontakty  # sprawdza czy klucz jest w słowniku
