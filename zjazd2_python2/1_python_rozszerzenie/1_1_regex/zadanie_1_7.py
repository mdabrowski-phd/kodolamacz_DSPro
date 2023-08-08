# 7. Napisz wyrażenie wyszukujące, czy w stringu znajduje się '*'

import re


super_string = 'moj super string z gwiazdka *'

moj_regex = re.compile(r'[*]')

if re.search(moj_regex, super_string):
    print(f"W '{super_string}' znajduje się '*'")
else:
    print(f"W '{super_string}' nie ma '*'")
