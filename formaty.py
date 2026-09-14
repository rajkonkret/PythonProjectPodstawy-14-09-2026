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
print(f"Witaj {user}, masz teraz {wiek} lat.")
# Witaj Tomek, masz teraz 39 lat.

print("Używamy wersji Pythona %i" % 3) # Używamy wersji Pythona 3
print("Używamy wersji Pythona %f" % 3) # Używamy wersji Pythona 3.000000
print("Używamy wersji Pythona %.2f" % 3.9) # Używamy wersji Pythona 3.90
print("Używamy wersji Pythona %.1f" % 3.9) # Używamy wersji Pythona 3.9
print("Używamy wersji Pythona %.0f" % 3.9) # Używamy wersji Pythona 4
print("Używamy wersji Pythona %.f" % 3.9) # Używamy wersji Pythona 4

