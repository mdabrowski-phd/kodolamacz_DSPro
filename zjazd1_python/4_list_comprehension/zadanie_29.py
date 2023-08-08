# Znajdź wszystkie słowa,
# które są krótsze niż 4 w napisie:
napis = "to jest moj super napis"

wynik = [wyraz for wyraz in napis.split() if len(wyraz) < 4]
print(wynik)
