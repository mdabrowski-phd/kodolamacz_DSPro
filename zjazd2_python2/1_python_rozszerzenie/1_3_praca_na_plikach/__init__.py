import pickle

# shift+ alt+e
# ctrl + /
# ## PLIKI TXT
#
f = open("my_file.txt", "w")  # ścieżka względna
for i in range(10):
    f.write(f"This is line {i}\n")
f.close()
#

f = open("my_file.txt", "r")
contents = f.read()
f.close()
print(type(contents))
print(contents)

# f = open("C:/Users/Oliwia/Pulpit/moj_plik", 'r')  # ścieżka bezwzględna
# contents = f.read()
# print(contents)


lines = [f"This is line {i}\n" for i in range(10)]

f = open("my_file.txt", "w")
f.writelines(lines)
f.close()
# #
f = open("my_file.txt", "r")
contents = f.readlines()
print(type(contents))
f.close()

for line in contents:
    print(f'linia : {line}')

# ---------------------------------------------
with open('my_file.txt', 'r') as my_file:
    contents = my_file.read()
# # tu juz nie moge np czegos zapisac ani czytac
print(contents)
print(my_file.closed)
#
with open('my_file.txt', 'w') as f:
    f.write('moj string')

#
with open('my_file.txt', 'a') as f:
    f.write('moj string\n')

# CZYTANIE PLIKU PO JEDNEJ LINII
with open("my_file.txt", "w") as f:
    for i in range(10):
        f.writelines(f"This is line {i}\n")

# rozwiazanie z petlą for:
with open("my_file.txt", "r") as f:
    contents = f.readlines()
    for line in contents:
        print(f'linia : {line}')

# uzycie petli while
with open("my_file.txt", "r") as f:
    line = f.readline()  # f.readline() reads a single line from the file
    while line:
        print(line)
        line = f.readline()

#
# ## ENCODE DECODE, CZYLI PROBLEMY Z JĘZYKIEM POLSKIM
with open('1_python_rozszerzenie/1_3_praca_na_plikach/files/polski.txt') as f:
    line = f.read()
    print(line)

#
with open('1_python_rozszerzenie/1_3_praca_na_plikach/files/polski.txt', 'r', encoding='utf8') as f:
    line = f.read()
    print(line)
#
with open('1_python_rozszerzenie/1_3_praca_na_plikach/files/polski.txt', 'r', encoding='windows-1250') as f:
    line = f.read()
    print(line)
# #
with open('1_python_rozszerzenie/1_3_praca_na_plikach/files/polski.txt', encoding="ascii") as f:
    line = f.read()
    print(line)
#
#
with open('1_python_rozszerzenie/1_3_praca_na_plikach/files/polski_2.txt', 'w', encoding="windows-1250") as f:
    f.write('Śledź żaden wątły nie jest.')

with open('1_python_rozszerzenie/1_3_praca_na_plikach/files/polski_2.txt', 'r', encoding="windows-1250") as f:
    line = f.read()
#
print(line)


#
#
# ## PLIKI JSON
import json

# https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/intro-to-tweet-json
#
my_dict = {
    "firstName": "Jane",
    "lastName": "Doe",
    "hobbies": ["running", "sky diving", "singing"],
    "age": 35,
    "children": [
        {
            "firstName": "Alice",
            "age": 6
        },
        {
            "firstName": "Bob",
            "age": 8
        }
    ]
}
# # #
with open("my_file_json.json", "w") as f:
    json.dump(my_dict, f)
#
with open("my_file_json.json", "r") as f:
    my_dict_2 = json.load(f)
#
print(type(my_dict_2))
print(my_dict_2['age'] == 35)
print(type(my_dict_2['hobbies']))
print(my_dict_2['hobbies'][0])

print(my_dict)

import pprint

pprint.pprint(my_dict)

print(json.dumps(my_dict, indent=4, sort_keys=True))
# https://jsonformatter.curiousconcept.com/
# #


# ## PLIKI PICKLE
#
import pickle

# #
my_dict = {
    "firstName": "Jane",
    "lastName": "Doe",
    "hobbies": ["running", "sky diving", "singing"],
    "age": 35,
    "children": [
        {
            "firstName": "Alice",
            "age": 6
        },
        {
            "firstName": "Bob",
            "age": 8
        }
    ]
}
with open('my_file_pickle.pickle', 'wb') as f:
    pickle.dump(my_dict, f)
#
with open('my_file_pickle.pickle', 'rb') as f:
    my_dict = pickle.load(f)
print(my_dict)
#
# # WARNING: https://docs.python.org/3/library/pickle.html
