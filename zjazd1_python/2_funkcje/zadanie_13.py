# Zadanie 13: Stwórz funkcje tworząca poniższy schemat:
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

# print('to jest\n koniec linii')

def trojkat_liczb(n):

    for i in range(1, n+1):
        for j in range(1, i+1):
            print(i, end=" ")

        print("")


trojkat_liczb(6)
