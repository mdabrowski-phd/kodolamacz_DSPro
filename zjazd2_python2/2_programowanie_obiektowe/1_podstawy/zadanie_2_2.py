# 3. Utwórz klasę o nazwie BankAccount, która reprezentuje konto bankowe,
# mając jako atrybuty:
# - liczba rachunków,
# - nazwa właściciela konta,
# - saldo.

# oraz metody:
# - wpłata (zwiększa saldo konta o podaną kwote)
# - wypłata (zmniejsza saldo konta o podaną kwote)
# - potrącenie salda o prowizje - prowizja banku wynosi 5% rachunku salda.
# - wyświetającą atrybuty konta

class BankAccount:

    def __init__(self, liczba_rachunkow, nazwa_wlasiciela, saldo=0):

        self.liczba_rachunkow = liczba_rachunkow
        self.nazwa_wlasciciela = nazwa_wlasiciela
        self.saldo = saldo

    def wplata(self, kwota):
        self.saldo += kwota

    def wyplata(self, kwota):
        self.saldo -= kwota

    def prowizja(self, prowizja=5):
        self.saldo -= self.saldo * prowizja / 100

    def wyswielt(self):
        print(f"Liczba rachunków: {self.liczba_rachunkow}, właściciel: {self.nazwa_wlasciciela}, saldo: {self.saldo}")


account = BankAccount(3, 'Michał', 50_000)
account.wplata(10_000)
account.prowizja()
account.wyswielt()

account.wyplata(37_000)
account.prowizja(10)
account.wyswielt()
