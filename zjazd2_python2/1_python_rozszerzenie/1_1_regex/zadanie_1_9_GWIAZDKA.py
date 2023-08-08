# 9. Napisz wyrażenie wyszukujące, czy w stringu znajdują się
# dwie samogłoski pod rząd (a,e,i,o,u)

import re


super_string = 'moaj supear string z gwiazdka *'
# super_string = 'moj supr string z gwazdka *'

moj_regex = re.compile(r'[aąeęoóuiyAEOUIY]{2}', flags=re.IGNORECASE)

if re.search(moj_regex, super_string):
    print(f"W '{super_string}' znajdują się dwie samogłoski pod rząd")
else:
    print(f"W '{super_string}' nie ma dwóch samogłosek pod rząd")
