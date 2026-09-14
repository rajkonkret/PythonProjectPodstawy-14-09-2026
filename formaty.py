user = "Tomek"  # str
wiek = 39  # int

wersja = 3.900001
print(type(wersja))  # <class 'float'> zmiennoprzecinkowe

liczba = 908765456321123  # int

print("Witaj %s, masz teraz %d lat." % (user, wiek))
# %d - digit (liczbowe)
# Witaj Tomek, masz teraz 39 lat.

# print("Witaj %d, masz teraz %s lat." % (user, wiek))
# TypeError: %d format: a real number is required, not str

# fstringiem