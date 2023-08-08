# todo
# Przetwórz plik timelog.txt, aby miał formę taką jak timelog_final.txt
# (odpowiednią ilość spacji można pominąć jak w pliku new_timelog.txt)

import datetime
import re


regex_time = re.compile(r'\d{2}:\d{2}')  # godzina
regex_activity = re.compile(r'\s.+')  # aktywność

# odczyt pliku po jednej linii
with open("data/timelog.txt", "r") as f:
    logi = f.read().splitlines()

logi_formatted = list()

# wydobycie przy użyciu regex czasu trwania aktywności
for log in logi:

    log_time = re.search(regex_time, log)
    log_activity = re.search(regex_activity, log)

    if log_time is not None:  # jeżeli niepusta linia ...

        log_time_dt = re.search(regex_time, log).group()
        log_time_dt = datetime.datetime.strptime(log_time_dt, "%H:%M")
        logi_formatted.append((log_time_dt, re.search(regex_activity, log).group()))

logi_time_dict = dict()

# zapis do pliku sformatej listy czas + aktywność
with open("data/timelog_MD.txt", "w") as f:

    for i in range(len(logi_formatted) - 1):  # ostatni element na liście to zawsze '_End'

        poczatek = logi_formatted[i][0]
        koniec = logi_formatted[i + 1][0]
        time_delta = koniec - poczatek

        if logi_formatted[i][1] == " End":  # pomijamy zakończenie aktywności, gdyż uwzględnione wcześniej
            f.writelines('\n')

        else:
            f.writelines(f'{datetime.datetime.strftime(poczatek, "%H:%M")}'
                         f'-{datetime.datetime.strftime(poczatek + time_delta, "%H:%M")}{logi_formatted[i][1]}\n')

            logi_time_dict[logi_formatted[i][1]] = logi_time_dict.get(logi_formatted[i][1],
                                                                      0) + time_delta.seconds // 60

total_time = sum([val for val in logi_time_dict.values()])  # całkowity czas wszystkich akywności

# uzupełnienie pliku o podsumowanie czasu kolejnych aktywności
with open("data/timelog_MD.txt", "a") as f:

    for key in sorted(logi_time_dict):
        f.writelines(f'\n{key[1:]}\t{logi_time_dict[key]} minutes {round(100 * logi_time_dict[key] / total_time)}%')
