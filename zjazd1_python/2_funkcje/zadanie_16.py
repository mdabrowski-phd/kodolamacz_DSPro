# ZADANIE 16: stwórz funkcję przyjmującą string,
# której wynikiem jest połączenie
# tego napisu ze swoim odbiciem lustrzanym np
# 'pies'->'piesseip

def dolacz_anagram(napis):

    return napis + napis[::-1]


input_str = "pies"
print(input_str)
print(dolacz_anagram(input_str))
