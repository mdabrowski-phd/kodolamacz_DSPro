# dla podanego stringu policz ilosc wystepowania
# litery 'a'
# (bez użycia .count).

string = 'Ala ma kota i dom'

# print(string.count('a'))
print(len([znak for znak in string if znak == "a"]))
