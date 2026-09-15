# instrukcje waarunkowe
# instrukcje sterowania przepływem programu
# if
# w zależności od warunku wykona jeden lub drugi blok programu

odp = True

if odp: print("Test")

if odp:
    # blok programu wykonany gdy warunek True
    print("Test")

# debugger - pozwala wykonać program krok po kroku
# pułapki - miejsce gdzie program się zatrzyma
odp = True

if odp:
    print("Brawo")
    print("Brawo")
    print("Brawo")
    print("Brawo")
    print("Brawo")
    print("Brawo")
    print("Brawo")
    print("Brawo")

print("Dalsza część programu")

odp = "Radek"  # True

if odp:  # bool(odp)
    print("Dane zostały wczytane")

if odp == "Radek":
    print("Jestem Radek")  # Jestem Radek

odp = 0
if odp:
    print("Działa")
else:  # wartość domyslna
    print("Zero -> False")

# a = "Radek"
a = "Tomek"

if a == "Radek":
    print("OK")
elif a == "Tomek":
    print("Też OK")
else:
    print("Nie znam Cię")

# Też OK

# pobrac zarobki
# jesli zarobki mniejsze niz 10000 -> podatek 0
# dla pozostałych podatek 90% (0.9)

# zarobki = int(input("Podaj zzarobki: "))
# podatek = 0
# print(zarobki)
#
# # kolejność ma znaczenie
# if zarobki < 10_000:
#     podatek = 0
# elif zarobki < 40_000:
#     podatek = 0.2
# elif zarobki < 100_000:
#     podatek = 0.4
# else:
#     podatek = 0.9
#
# # 0.2 dla zarobków 10000 i mniej niz 40000
# print(f"Podatek wynosi: {zarobki * podatek:.2f} pln.")
# Podaj zzarobki: 56789
# 56789
# Podatek wynosi: 22715.600000000002 pln.

# Podaj zzarobki: 56789
# 56789
# Podatek wynosi: 22715.60 pln.

sum_zam = 170

if sum_zam > 150:
    rabat = 25
else:
    rabat = 0

# Rabat wynosi: 25
print(f"Rabat wynosi: {rabat}")

# operator warunkowy
rabat = 25 if sum_zam > 150 else 0
print(f"Rabat wynosi: {rabat}")  # Rabat wynosi: 25

# napisac zadanie test z...
# try pytania
# punktacja

punkty = 0
odp = input("Czy pada deszcz? ")

if odp.strip().casefold() == "tak".strip().casefold():
    print("Weź parasol")
    # punkty = punkty + 1
    punkty += 1
else:
    print("Idz")

odp = input("Podaj stolicę Polski: ")

if odp.strip().casefold() == "Warszawa".strip().casefold():
    print("Odpowiedź prawidłowa")
    punkty += 1
else:
    print("Poszukaj w książce")

print("Punkty:", punkty)
# spam += 1    spam = spam + 1
# spam -= 1    spam = spam - 1
# spam *= 1    spam = spam * 1
# spam /= 1    spam = spam / 1
# spam %= 1    spam = spam % 1

# Czy pada deszcz? tak
# Weź parasol
# Podaj stolicę Polski: Warszawa
# Odpowiedź prawidłowa
# Punkty: 2