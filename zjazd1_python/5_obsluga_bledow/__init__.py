def division():
    try:
        a = 2
        b = 0
        print(a / b)
    except Exception as e:
        print("blad ", e)


try:
    print(x)
except NameError:
    print("Variable x is not defined")
except Exception:
    print("Something else went wrong")

try:
    print("Hello")
except ZeroDivisionError as e:
    print("Something went wrong")
else:  # jesli nie ma błędu
    print("Nothing went wrong")

try:
    print(x)
except Exception:
    print("Something went wrong")
finally:  # wykona sie niezależnie od błędu
    print("The 'try except' is finished")

# mozemy tez sami decydowac kiedy chcemy wywołac błąd
x = -1
if x < 0:
    raise Exception("Sorry, no numbers below zero")

x = "hello"
if not type(x) is int:
    raise TypeError("Only integers are allowed")

# lista wszystkich wyjątkow wbudowanych
# https://docs.python.org/3/library/exceptions.html
