import pandas as pd
import requests

USERS_URL = 'https://reqres.in/api/users?page='
SINGLE_USER_URL = 'https://reqres.in/api/users/'
LOGIN_URL = 'https://reqres.in/api/login'

def test_load_all_pages():
    """
    Wczytaj wszystkie strony z API którego adres znajduje się zmiennej USERS_URL.
    Zwróc uwagę na parametr pages.
    API zwraca, razem z danymi, informację ile stron jest dostępne.

    W wyniku powinien powstać jeden DataFrame zawierający dane ze wszystkich stron.
    """
    response = requests.get(USERS_URL + '1').json()
    total_pages = response['total_pages']

    dfs = []
    for i in range(1, total_pages + 1):

        response = requests.get(USERS_URL + str(i)).json()
        dfs.append(pd.DataFrame(response['data']))

    df = pd.concat(dfs).reset_index(drop=True)
    print(df)

    assert df.shape == (12, 5)
    assert set(df['email'].values) == {
        'byron.fields@reqres.in',
        'charles.morris@reqres.in',
        'emma.wong@reqres.in',
        'eve.holt@reqres.in',
        'george.bluth@reqres.in',
        'george.edwards@reqres.in',
        'janet.weaver@reqres.in',
        'lindsay.ferguson@reqres.in',
        'michael.lawson@reqres.in',
        'rachel.howell@reqres.in',
        'tobias.funke@reqres.in',
        'tracey.ramos@reqres.in'
    }

def test_load_single_page_and_handle_missing_data():
    """
    1. Wczytaj stronę z danymi użytkowników o id: 2, 7, 22.
    2. Zwrócony wynik zawiera email użytkownika. Dodaj wszystkie adresy email do listy emails.
    3. Jeżeli strona danego użytkownika nie istnieje, dodaj do listy emails wartość None.
    """
    emails = []
    for user_ID in [2, 7, 22]:

        response = requests.get(SINGLE_USER_URL + str(user_ID))

        if response.status_code == 200:
            emails.append(response.json()['data']['email'])
        else:
            emails.append(None)

    print(emails)
    assert emails == ['janet.weaver@reqres.in', 'michael.lawson@reqres.in', None]

def test_create_a_new_user():
    """
    Użyj metody POST do utworzenia nowego użytkownika.
    Wysłane zapytanie powinno zawierać dane w formacie JSON w następującej postaci:
    {
        "name": "Bolesław I Chrobry",
        "job": "king"
    }
    W zmiennej user_id umiejść id utworzonego użytkownika zwrócony przez API.
    """
    new_user = {
        "name": "Bolesław I Chrobry",
        "job": "king"
    }

    response = requests.post(SINGLE_USER_URL, json=new_user).json()
    user_id = response['id']

    print(user_id)
    assert int(user_id) > 11

def test_login():
    """Zaloguj się do API wysyłając zapytanie POST do LOGIN_URL.
    W zapytaniu umiejść obiekt JSON zawierający pola email i password.
    W polu emails wpisz "eve.holt@reqres.in", zawartość pola "password" nie ma znaczenia. Można wpisać "abc".
    W odpowiedzi otrzymasz token, zapisz go w zmiennej token.
    """
    login = {
        'email': 'eve.holt@reqres.in',
        'password': 'abc'
    }

    data = requests.post(LOGIN_URL, json=login)  # czasem trzeba dodać parametr 'headers'
    token = data.json()['token']

    assert len(token) == 17