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

print("Używamy wersji Pythona %i" % 3)  # Używamy wersji Pythona 3
print("Używamy wersji Pythona %f" % 3)  # Używamy wersji Pythona 3.000000
print("Używamy wersji Pythona %.2f" % 3.9)  # Używamy wersji Pythona 3.90
print("Używamy wersji Pythona %.1f" % 3.9)  # Używamy wersji Pythona 3.9
print("Używamy wersji Pythona %.0f" % 3.9)  # Używamy wersji Pythona 4
print("Używamy wersji Pythona %.f" % 3.9)  # Używamy wersji Pythona 4

print(f"Używamy wersji pythona {wersja}")  # Używamy wersji pythona 3.900001
print(f"Używamy wersji pythona {wersja:.2f}")  # Używamy wersji pythona 3.90
print(f"Używamy wersji pythona {wersja:.1f}")  # Używamy wersji pythona 3.9
print(f"Używamy wersji pythona {wersja:.0f}")  # Używamy wersji pythona 4

print(wersja)  # 3.900001 zmienna się nie zmieniła

print(f"{user:<10}")  # "Tomek     "
print(f"{user:>20}")  # "               Tomek"
print(f"{user:^15}")  # "     Tomek     "
print(f"{user:.^15}")  # ".....Tomek....."

print(liczba)  # 908765456321123

print(f"Nasza duża liczba: {liczba:,}")  # Nasza duża liczba: 908,765,456,321,123
print(f"Nasza duża liczba: {liczba:_}")  # Nasza duża liczba: 908_765_456_321_123
print(f"Nasza duża liczba: {liczba:_}".replace("_", " "))  # Nasza duża liczba: 908 765 456 321 123

liczba = 150_000_000_000
print(type(liczba))  # <class 'int'>
print(liczba)  # 150000000000
