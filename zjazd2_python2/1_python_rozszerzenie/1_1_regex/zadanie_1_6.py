# # 6. Napisz wyrażenie wyszukujące, czy w stringu znajduje się 'q' lub 'Q'

import re


super_string = ',kwa kwa qua'

moj_regex = re.compile(r'q', flags=re.IGNORECASE)


if re.search(moj_regex, super_string):
    print(f"W '{super_string}' znajduje się 'q' lub 'Q'")
else:
    print(f"W '{super_string}' nie ma 'q' lub 'Q'")
