# # 2. Znajdź jedynie imiona żeńskie

import re


imiona = 'Balbina, Barbara, Beata, Berenika, Bernadeta, Bianka, Blanka, Bogda, Bogna, Bogumiła, Bogusława, Edyta, ' \
 'Bartłomiej, Bartosz, Bastian, Beniamin, Benjamin, Bernard, Błażej, Bogumił, Bolesław, Borys, Bożydar, ' \
 'Brajan, Eftalia, Elena, Eleonora, Eliza, Elwira, Jadwiga, Jagna, Jagoda, Jana, Janina, Jaśmina, Leokadia, ' \
 'Jessica, Joanna, Jola, Jacek, Jacob, Jakub, Jan, Janusz, Jarosław, Jeremi, Jeremiasz, Jerzy, Jędrzej, Joachim'


moj_regex = re.compile(r'\w+a\b')  # \b - oddzielne słowo, ignoruje przecinki
print(re.findall(moj_regex, imiona))
