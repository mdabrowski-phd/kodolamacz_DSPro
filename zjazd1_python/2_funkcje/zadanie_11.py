# ZADANIE 11: napisz funkcje przyjmującą string.
# Policz ile razy
# znajduje się słowo "usa", niezależnie od wielkości
# liter

def policz_usa(napis):
    return napis.lower().count("usa")


input_str = "USA trusa uSa bUSa kotus ala"
print(policz_usa(input_str))
