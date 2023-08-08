# 3. Stwórz słownik, ile razy występuje jak długi ciąg liter 'i' w napisie

import re
from collections import Counter


super_napis = 'piigiiiihiiiiiiiihihihihiffffffiiiiiiiiiiikikikikikikiloiiiiiiiiiiiiiaaaaaaapppppppppppppppp' \
              'yyyyyyyyyyyyhihihihihihiiiiiiii'

dict_ile = re.findall(r'i+', super_napis)
print(Counter(dict_ile))  # alternatywnie można użyć "dict_comprehension": {k: dict_ile.count(k) for k in dict_ile}
