"""
Stwórz grę w stylu mortal-combat, gdzie zawodnikami będa obiekty naszych klas (czyli np hero = Superhero()).
W każdej rundzie losowane maja być dwie postacie (dwóch superbohaterów, czyli dwa obiekty). Każdy z nich może walczyć
losową bronią z superpowers (należy ja wylosować) oraz zadać losową ilość punktów obrażeń z zakresu 1-10 (funkcja
attack). Ten gracz, który wylosuje większą ilość obrażeń, obniża life_points przeciwnikowi o swoją liczbę obrażeń
minus liczba, którą wylosował przeciwnik, np. gracz S1 zadaje 5 punków obrażeń, zaś	gracz S2 zadaje 6 punków obrażeń
=> w efekcie wygrywa gracz S2 i zadaje 1 (czyli 6 minus 5) punkty obrażeń. Po ataku należy zaktualizować liczbę
punktów życia przegranego. Jeśli wyniesie ona <=0 gracz taki odpada z gry. Gra trwa do momentu, gdy zostanie ostatni
gracz (on oczywiście wygrywa;-) ). Jeśli dwóch graczy zada takie same obrażenia, nikt nie odnosi obrażeń i odbywa się
ponowne losowanie dwóch graczy.
"""

from zadanie_3_1_Michal import superman
from zadanie_maciek import angry_cat
from zadanie_3_1_piotr import super_hero_1
from zadanie_3_1_eryk_k import uliczny_zakapior
from zadanie_3_1_oliwia import super_ciastko
from zadanie_3_1_Eryk_L import super_herosik_komarek
from SuperHero_Filip import Fil
from Łukasz_bohater import czlowiek_robak
from zadanie_3_1_Damian_K_ import klik_bochater

from random import sample


def play_fight(heroes):

    cur_heroes = sample(heroes, 2)
    attack0 = cur_heroes[0].attack()
    attack1 = cur_heroes[1].attack()

    print(f"Zawodnik 1: {cur_heroes[0].name}, życie: {cur_heroes[0].life_points}, atak: {attack0}")
    print(f"Zawodnik 2: {cur_heroes[1].name}, życie: {cur_heroes[1].life_points}, atak: {attack1}")

    if attack0 > attack1:

        cur_heroes[1].decrease_life(attack0 - attack1)
        print(f"Zawodnik {cur_heroes[1].name} traci {attack0 - attack1} życia.")

        if cur_heroes[1].life_points <= 0:

            print(f"Zawodnik {cur_heroes[1].name} ginie. Odpada z turnieju.")
            heroes.remove(cur_heroes[1])

    elif attack0 < attack1:

        cur_heroes[0].decrease_life(attack1 - attack0)
        print(f"Zawodnik {cur_heroes[0].name} traci {attack1 - attack0} życia.")

        if cur_heroes[0].life_points <= 0:

            print(f"Zawodnik {cur_heroes[0].name} ginie. Odpada z turnieju.")
            heroes.remove(cur_heroes[0])

    else:
        print("Remis, nikt nie odpada. Czas na kolejną rundę!")


def main():

    super_heroes = [klik_bochater, czlowiek_robak, Fil, super_herosik_komarek, super_ciastko, uliczny_zakapior,
                    super_hero_1, angry_cat, superman]

    runda = 1
    while len(super_heroes) > 1:

        print(f"\n----- Runda {runda} -----")
        play_fight(super_heroes)
        runda += 1

    print(f"\n**********\nTurniej wygrywa: {super_heroes[0].name}, pozostałe życie: {super_heroes[0].life_points}\n"
          f"A to wszystko dzięki umiejętnościom: {super_heroes[0].superpowers}")


if __name__ == "__main__":
    main()
