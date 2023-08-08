# Znajdź wszystkie liczby od 10 do 30,
# które zawierają cyfre 3

numery = list(range(10, 31))

# wynik = [numer for numer in numery if str(numer).find('3') != -1]
wynik = [numer for numer in numery if '3' in str(numer)]
print(wynik)
