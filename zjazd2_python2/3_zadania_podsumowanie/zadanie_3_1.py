# todo
# Na podstawie pliku 'apache_access.log' policz ile było zapytań GET z
# adresu localhost (127.0.0.1) pomiędzy 10:40 a 10:55 ()

import re
import datetime
# import pytz # ekstra dodatek, ale nie trzeba bylo uzyc

moj_regex_ip = re.compile(r'127.0.0.1\b')
moj_regex_time = re.compile(r'\[.*]')

with open("data/apache_access.log") as f:
    logi = f.readlines()

dobre_logi = 0

for log in logi:

    if re.search(moj_regex_ip, log):

        log_time = re.search(moj_regex_time, log).group()[1:-1]
        time = datetime.datetime.strptime(log_time, "%d/%b/%Y:%H:%M:%S +0300")

        if time.hour == 10 and 45 < time.minute < 55:
            dobre_logi += 1

print(f"Liczba szukanych logów: {dobre_logi}")
