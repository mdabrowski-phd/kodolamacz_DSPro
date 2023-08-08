lista = [1, 2, 3]
for x in lista:
    print(x)

for x in range(10):
    print(x)

for x in range(2, 10, 2):
    print(x)

# break i continue
for val in "napis":
    if val == "i":
        break
    print(val)

for val in "napis":
    if val == "i":
        continue
    print(val)

# zip i enumerate
name_list = ['adam', 'anna', 'hanna']
for num, name in enumerate(name_list):
    print(num, name)

city_list = ['warsaw', 'london', 'new york']

for name, city in zip(name_list, city_list):
    print(name, city)
