import pandas as pd
import sqlite3
import requests
from bs4 import BeautifulSoup

"""1. Z bazy danych znajdującej się w pliku data/sql/titanic.db (w katalogu roboczym używanym wczoraj), pobierz dane 
wszystkich osób, które przeżyły katastrofę Titanica i w czasie katastrofy miały powyżej 35 lat."""

con = sqlite3.connect('tests/sql/data/sql/titanic.db')
query = """SELECT * FROM passengers p JOIN survivors s ON p.PassengerID = s.PassengerID
            JOIN tickets t ON t.PassengerId = p.PassengerId WHERE Survived=1 AND Age>35"""

try:
    tic_df = pd.read_sql_query(query, con)
finally:
    con.close()

"""2. Na stronie https://en.wikipedia.org/wiki/Passengers_of_the_Titanic znajdź wszystkie osoby, które przeżyły.
Połącz dane z naszej bazy danych z linkami do stron Wikipedii o tych osobach. Interesują nas tylko osoby znajdujące 
sie w obu zbiorach danych (ich nazwiska zostały zapisane w identyczny sposób w obu listach)."""

response = requests.get('https://en.wikipedia.org/wiki/Passengers_of_the_Titanic')
soup = BeautifulSoup(response.text, 'html.parser')

urls = []
links = [el.find('a') for el in soup.find_all('tr', {'style': 'background:#9bddff;'}) if el.find('a')]

for link in links:
    if link.text in tic_df.Name.tolist():
        urls.append((f"https://en.wikipedia.org/{link.get('href')}", link.text))

"""3. Otwórz stronę Wikipedii dla każdej osoby. Z prawej strony znajduje się prostokąt z podsumowaniem. Pobierz z 
niego wszystkie dane. Po pobraniu wszystkich osób zapisz dane z Wikipedii i bazy danych w jednym pliku XLS."""

dfs_to_save = []
for url, name in urls:

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    df = pd.read_html(str(soup.find_all('table', {'class': 'infobox'})))[0]
    df.columns = ['Attribute', 'Value']

    db_df = tic_df[tic_df.Name == name].drop('index', axis=1).transpose().reset_index()
    db_df.columns = ['Attribute', 'Value']

    dfs_to_save.append((pd.concat([df, db_df]), name))

"""4. Dane o każdej osobie powinny znaleźć się w osobnej zakładce arkusza (nazwanej nazwiskiem i imieniem tej osoby). 
Każda zakładka powinna zawierać  dwie kolumny: nazwa atrybutu i wartość (bez nagłówków i bez indeksu)"""

writer = pd.ExcelWriter('excel_titanic.xlsx', engine='xlsxwriter')
[df.to_excel(writer, sheet_name=name, index=False) for df, name in dfs_to_save]
writer.save()
