# #!/usr/bin/env python
# # coding: utf-8
#
# # # PRACA Z DATAMI
#
# # ## Tworzenie zmiennych czasowych
#
#
import datetime
# from datetime import datetime
from dateutil.parser import parse  # pip install python-dateutil

#
# print("1 Hour")
print(datetime.time(1))
# #
# print("2 and a half hour")
print(datetime.time(2, 30))
# #
# print("3 hours, 45 minutes and 30 seconds")
dummy_t = datetime.time(3, 45, 30)
print(type(dummy_t))
#

dummy = datetime.datetime(2022, 4, 9, 22, 19)
print(type(dummy))
print(dummy)
#

ts_now = datetime.datetime.now()
print(ts_now)
# #
# # #
print(ts_now.day)
#
print(ts_now.year)
print(ts_now.month)
print(ts_now.minute)
print(ts_now.second)
print(ts_now.microsecond)

print(ts_now.isoweekday())
#
ts_xmas = datetime.datetime(2023, 12, 24)
print(type(ts_xmas))
print(ts_xmas)
# # #
ts_now = datetime.datetime.now()
ts_diff = ts_xmas - ts_now
print(ts_diff)
print(type(ts_diff))
# #
# #
today = datetime.datetime.now()
offset = datetime.timedelta(days=45, hours=13)
print(today + offset)
#
#
# # ## KONWERSJA STRINGÓW I DAT
# # - %Y year
# # - %d day
# # - %m month
# # - %H hour
# # - %M minute
# # - %S second
#
#
date_str = "01-20-2015T14:34"
date_ts = datetime.datetime.strptime(date_str, "%m-%d-%YT%H:%M")
print(date_ts)
print(type(date_ts))
#
date_str = "10/01/2015"
date_ts = datetime.datetime.strptime(date_str, "%d/%m/%Y")
print(date_ts)
print(type(date_ts))
#
# 2015-01-10 00:00:00
new_date_str = datetime.datetime.strftime(date_ts, "%H:%M:%S %m-%d-%Y")
print(new_date_str)
print(type(new_date_str))
# #
# #
print(f'{date_ts.month}-{date_ts.year}')
print(str(date_ts))
#
#
# from datetime import datetime
# new_date_str = datetime.strftime(date_ts, "%H:%M:%S %m-%d-%Y")
# print(new_date_str)
# print(type(new_date_str))

#
# # PARSE
#
# from dateutil.parser import parse  # pip install python-dateutil

print(parse('January 31, 2010'))
print(parse("2003-01-04T10:49:41"))
#
# # https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
