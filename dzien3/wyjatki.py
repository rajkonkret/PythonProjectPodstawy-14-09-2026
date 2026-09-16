# wyjątki - błedy podczas wykonywania proggramu

# print(5 / 0)
# Traceback (most recent call last):
#   File "C:\Users\CSComarch\PycharmProjects\PythonProjectPodstawy-14-09-2026\dzien3\wyjatki.py", line 3, in <module>
#     print(5 / 0)
#           ~~^~~
# ZeroDivisionError: division by zero

# zrzutowac litere na cyfrę i obsłużyc błąd
try:
    # print(5 / 0)
    # int('A') # ValueError: invalid literal for int() with base 10: 'A'
    # raise KeyError("Bład Klucza")
    wynik = 20 / 3
except ZeroDivisionError:
    print('Nie dziel przez zero')
except ValueError:
    print("Błąd wartości")
except Exception as e:  # pozozostałe błędy
    print("Bład:", e)
else:  # kiedy niema błedu
    print("Wynik:", wynik)
finally:  # wykona się zawsze
    print('Kolejne obliczenia')

# print(wynik)
print('Dalsza część programu')
# Nie dziel przez zero
# Dalsza część programu

# Wynik: 6.666666666666667
# Kolejne obliczenia
# Dalsza część programu
