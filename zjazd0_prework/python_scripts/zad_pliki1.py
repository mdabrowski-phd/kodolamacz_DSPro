def main():

    sciezka_do_odczytu = r"E:\DataSciencePRO\zad1.py"
    sciezka_do_zapisu = r"E:\DataSciencePRO\zad1_liczba_linii2.txt"

    try:
        with open(sciezka_do_odczytu) as plik_odczyt:

            for i, line in enumerate(plik_odczyt):
                print(line, end="")

            print(f"\nLiczba linii: {i+1}")

            with open(sciezka_do_zapisu, "w") as plik_zapis:
                plik_zapis.writelines([f"Plik: {sciezka_do_odczytu}", f"\nLiczba linii: {i+1}"])

    except FileNotFoundError as e:
        print("Plik do odczytu nie istnieje!")
        print(e)


if __name__ == "__main__":
    main()
