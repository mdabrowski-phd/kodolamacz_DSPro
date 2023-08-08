# Usun wszystkie samogloski z napisu
napis = "Ala ma Kota i dom"

wynik = "".join([litera for litera in napis.lower() if litera not in ['a', 'e', 'i', 'o', 'u', 'y', 'ą', 'ę', 'ó']])
print(wynik)
