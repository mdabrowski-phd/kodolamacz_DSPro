# 2. Zamień poniższą datę na: ’31 January, 2001, Wednesday’

import datetime


dt = datetime.datetime(2001, 1, 31)
dt_str = datetime.datetime.strftime(dt, "%d %B, %Y, %A")

print(dt_str)
