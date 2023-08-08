# ZADANIE 7: napisz funkcję przyjmującą string z wielkimi
#  i małymi literami,
# zwróć nowy string, który będzie zawierał najpierw małe
# potem wielkie litery napisu.
# ‘DoM jESt’ > ‘ojtDMES’

def sortuj_napis(napis):

    output_str = list()

    for znak in napis:
        if znak.islower():
            output_str.append(znak)

    for znak in napis:
        if znak.isupper():
            output_str.append(znak)

    return ''.join(output_str)


inputStr = "DoM jESt"
wynik = sortuj_napis(inputStr)

print(inputStr)
print(wynik)
