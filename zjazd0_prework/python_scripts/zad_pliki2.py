import os
import datetime


def stworz_plik(sciezka, rozmiar):

    f = open(sciezka, "w")
    f.write("A" * rozmiar)
    f.close()


def main():

    sciezka_do_folderu = r"E:\DataSciencePRO\restored"
    # stworz_plik (sciezka_do_folderu + "\\plik_duzy1.txt", 500 * 1024)

    try:
        for plik in os.listdir(sciezka_do_folderu):

            sciezka_do_pliku = os.path.join(sciezka_do_folderu, plik)
            (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat(sciezka_do_pliku)
            data_modyfikacji = datetime.datetime.now() - datetime.datetime.fromtimestamp(mtime)

            if size > 1_000_000 or data_modyfikacji.days > 1000:
                # print(f"Usuwam plik: {sciezka_do_pliku}")
                os.remove(sciezka_do_pliku)

    except FileNotFoundError:
        print("Podana ścieżka nie istnieje")


if __name__ == "__main__":
    main()
