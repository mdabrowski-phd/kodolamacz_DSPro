# 5. W poniższej liście dat znajdź najstarszą.
# Wyświetl czas, jaki upłynął od tej chwili do teraz w sekundach

import datetime


datetime_list = ['25.08.1995 00:00:00', '22.07.1999 00:00:00', '01.01.2001 13:42:59', '13.12.2011 01:02:03']

past = min([datetime.datetime.strptime(data, "%d.%m.%Y %H:%M:%S") for data in datetime_list])
print(past)

now = datetime.datetime.now()
print(round((now - past).total_seconds()))
