# 3. Stwórz zmienną, która jest różnicą czasu future i chwili obecnej.
# wynik wyświetl w sekundach

import datetime


future = datetime.datetime(2023, 3, 5, 16, 00)
delta = future - datetime.datetime.now()

print(round(delta.total_seconds()))
