# # 5. Zamień domene z adresów mailowych na onet.pl

import re


napis = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher super_user@gmail.com'

moj_regex = re.compile(r'@\w+\.\w+')
print(re.sub(moj_regex, '@onet.pl', napis))
