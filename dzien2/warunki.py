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
    print("Jestem Radek") # Jestem Radek

odp = 0
if odp:
    print("Działa")
else: # wartość domyslna
    print("Zero -> False")

# a = "Radek"
a = "Tomek"

if a =="Radek":
    print("OK")
elif a == "Tomek":
    print("Też OK")
else:
    print("Nie znam Cię")

# Też OK