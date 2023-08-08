# 2. Stwórz klase DateMonthly, która dla podanej daty będzie obliczała:
# - begin_date - początek miesiąca tj dla 16 marca -> 1 marca godzina 00:00:00
# - end_date - koniec miesiaca tj dla 16 marca -> 31 marca, dla 16 kwietnia -> 30 kwietnia godzina 23:59:59:999999
# - previous_end_date - koniec poprzedniego miesiąca tj dla 16 kwietnia -> 31 marca godzina 23:59:59:999999

# https://docs.python.org/3/library/calendar.html

import datetime
from calendar import monthrange


class DateMonthly:

    def __init__(self, data):
        self.data = data

    def begin_date(self):
        return datetime.datetime.strftime(self.data, "%Y-%m-01 00:00:00")

    def end_date(self):
        ostatni_dzien = monthrange(self.data.year, self.data.month)[1]
        return datetime.datetime.strftime(self.data, f"%Y-%m-{ostatni_dzien} 23:59:59:999999")

    def previous_end_date(self):

        if self.data.month == 1:
            poprzedni_rok = self.data.year - 1
            return datetime.datetime.strftime(self.data, f"{poprzedni_rok}-12-31 23:59:59:999999")

        else:
            ostatni_dzien = monthrange(self.data.year, self.data.month-1)[1]
            return datetime.datetime.strftime(self.data, f"%Y-%m-{ostatni_dzien} 23:59:59:999999")


dummy = datetime.datetime(2023, 3, 5)
date_monthly_1 = DateMonthly(dummy)
print(date_monthly_1.data)

print(date_monthly_1.begin_date())
print(date_monthly_1.end_date())
print(date_monthly_1.previous_end_date())

print("---")

dummy2 = datetime.datetime(2023, 1, 12)
date_monthly_2 = DateMonthly(dummy2)
print(date_monthly_2.data)

print(date_monthly_2.begin_date())
print(date_monthly_2.end_date())
print(date_monthly_2.previous_end_date())
