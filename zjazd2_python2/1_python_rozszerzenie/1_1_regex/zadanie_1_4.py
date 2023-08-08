# 4. Znajdź adresy mailowe

import re


napis = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher super_user@gmail.com'

moj_regex = re.compile(r'\w+@\w+[.]\w+')  # można użyć \. zamiast [.]
print(re.findall(moj_regex, napis))
