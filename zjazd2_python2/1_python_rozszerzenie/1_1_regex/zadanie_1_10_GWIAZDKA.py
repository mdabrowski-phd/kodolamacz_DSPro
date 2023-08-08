# # 10. Napisz wyrażenie wyszukujące, czy w stringu znajduje się przynajmniej 6 cyfr (w sumie)

import re


dlugi_string = '* 345445 ja'
krotki_string = '12 ja 45 on 6 ty'

super_string = dlugi_string  # krotki_string

if len(re.findall(r'\d', super_string)) >= 6:
    print(f"W '{super_string}' znajduje się w sumie przynajmniej 6 cyfr")
else:
    print(f"W '{super_string}' nie ma w sumie przynajmniej 6 cyfr")
