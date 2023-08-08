# Popraw poniszy kod wykorzystując:
# ZeroDivisionError, ValueError, IndexError, TypeError.

# def example1():
#     x = int(input("enter a number: "))
#     y = int(input("enter another number: "))
#     print(x / y)


# def example2(lista):
#     suma = []
#     for i in range(len(lista)):
#         suma.append(lista[i] + lista[i + 1])
#         print(suma)


def example1():

    try:

        x = int(input("enter a number: "))
        y = int(input("enter another number: "))
        print(x / y)

    except ZeroDivisionError:
        print("Niedozwolone dzielenie przez zero!")

    except ValueError:
        print("Niepoprawne argumenty!")


def example2(lista):

    suma = []
    for i in range(len(lista)):
        try:
            suma.append(lista[i] + lista[i + 1])

        except TypeError:
            print("Niepoprawne argumenty!")

        except IndexError:
            print("Indeks spoza zakresu!")

        finally:
            print(suma)


print("---example1---")
example1()

print("---example2---")
liczby = [1, 2, 3, 4, 5]
example2(liczby)
