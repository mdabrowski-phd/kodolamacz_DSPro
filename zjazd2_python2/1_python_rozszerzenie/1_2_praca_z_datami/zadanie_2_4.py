# 4. Zamień napis 'Jan 20, 2017 5pm' na zmienną typu czas

import datetime

s = 'Jan 20, 2017 5pm'

s_dt = datetime.datetime.strptime(s, "%b %d, %Y %I%p")
print(s_dt)
print(type(s_dt))
