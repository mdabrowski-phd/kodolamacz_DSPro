# ZADANIE 1: zaprojektuj program, który w zależności od podanego przez użytkownika
# imienia wyświetli, czy użytkownik jest kobietą (imię kończy się na litere a),
# mężczyzną (imię nie kończy się na litere a), czy podał pusty string
print('podaj imie:')
imie = input()

if imie == "":
    print("Pusty napis!")

elif imie.endswith('a'):
    print(f"Użytkownik {imie} prawdopodobnie jest kobietą.")

else:
    print(f"Użytkownik {imie} prawdopodobnie jest mężczyzną.")
