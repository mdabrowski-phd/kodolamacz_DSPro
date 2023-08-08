def sprytna_potega(podstawa, wykladnik):

    if wykladnik == 0:
        return 1
    elif wykladnik % 2 == 0:
        return sprytna_potega(podstawa, wykladnik//2) * sprytna_potega(podstawa, wykladnik//2)
    else:
        return sprytna_potega(podstawa, wykladnik//2) * sprytna_potega(podstawa, wykladnik//2) * podstawa


def czy_palindrom(napis):

    for i in range(len(napis)//2):
        if napis[i] != napis[-i-1]:  # indeksy ujemne odliczają od końca napisu; inaczej: len(napis)-i-1
            return False

    return True


""" inny sposób, odwrócenie napisu
# def czy_palindrom(napis):
#     return napis == napis[::-1]
"""


def czy_anagram(napis1, napis2):

    if len(napis1) != len(napis2):
        return False

    dict1 = dict()
    dict2 = dict()

    for znak1, znak2 in zip(napis1, napis2):

        if znak1 in dict1:
            dict1[znak1] += 1
        else:
            dict1[znak1] = 1

        if znak2 in dict2:
            dict2[znak2] += 1
        else:
            dict2[znak2] = 1

    return dict1 == dict2


""" inny sposób, sortowanie znaków napisu
# def czy_anagram(napis1, napis2):
#     return sorted(napis1) == sorted(napis2)
"""


def moda_lista(lista):

    zliczenia = dict()

    for el in lista:
        zliczenia[el] = zliczenia.get(el, 0) + 1

    return max(zliczenia, key=lambda k: zliczenia[k])


""" inny sposób, tradycyjne szukanie maksimum na liście
# def moda_lista(lista):
# 
#     zliczenia = dict()
# 
#     for el in lista:
#         zliczenia[el] = zliczenia.get(el, 0) + 1
# 
# 
#     el_maks = lista[0]
#     ile_maks = zliczenia[lista[0]]
# 
#     for el, ile in zliczenia.items():
#         if ile > ile_maks:
#             el_maks, ile_maks = el, ile
# 
#     return el_maks
"""


def main():

    print("---sprytna_potega---")
    print(sprytna_potega(2, 7))
    print(sprytna_potega(2, 6))
    print(sprytna_potega(2, 1))
    print(sprytna_potega(2, 0))
    print(sprytna_potega(3, 5))
    print(sprytna_potega(3, 2))

    print("---czy_palindrom---")
    print(czy_palindrom("xyzyx"))
    print(czy_palindrom("abcdcba"))
    print(czy_palindrom("ABCBCEA"))

    print("---czy_anagram---")
    print(czy_anagram("abc", "cab"))
    print(czy_anagram("kot", "kotek"))
    print(czy_anagram("razdwa", "dwaraz"))
    print(czy_anagram("raz dwa", "dwaraz"))

    print("---moda_lista---")
    print(moda_lista([1, 2, 2, 3, 1, 2, 2, 3]))
    print(moda_lista([1, 10, 3, 5, 3]))


if __name__ == "__main__":
    main()
