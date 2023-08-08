# 3. Napisz program zliczający wiek wszystkich superbohaterów
# spisanych w pliku superhero.json.

import json


with open('files/superhero.json', 'r') as f:
    super_heroes = json.load(f)

wiek_suma = 0
for member in super_heroes["members"]:
    wiek_suma += member["age"]

print(wiek_suma)
