# ZADANIE 2: w podanym napisie wyświetl wszystkie slowa
# na literę "a":
napis = 'ala ma kota ale nie ma psa'

for wyraz in napis.split():
    if wyraz.startswith("a"):
        print(wyraz)
