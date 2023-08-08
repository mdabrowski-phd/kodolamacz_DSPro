# ZADANIE 17: napisz funkcję, która będzie przyjmowała napis,
# a zwracała jego elementy w odwrotnej kolejności np
# "pies je kiełbase'-> 'kiełbase je pies’

def odwroc_napis(napis):

    wyrazy = napis.split()

    anagram = list()
    for i in range(0, -len(wyrazy), -1):
        anagram.append(wyrazy[i-1])

    return " ".join(anagram)


input_str = "pies je kiełbase"
print(input_str)
print(odwroc_napis(input_str))
