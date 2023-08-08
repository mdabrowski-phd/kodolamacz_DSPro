# # 6. Ile minęło sobót pomiędzy dwoma poniższymi datami, które przypadają na dzień miesiąca podzielny przez 3?
# (odp: 14)

import datetime


d1 = datetime.date(1869, 1, 2)
d2 = datetime.date(1869, 10, 2)

# print(d1.isoweekday())
specjalne_soboty = 0

while d1 < d2:

    if d1.day % 3 == 0:
        specjalne_soboty += 1

    d1 += datetime.timedelta(days=7)

print(specjalne_soboty)
