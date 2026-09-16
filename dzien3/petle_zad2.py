from dzien2.typy_danych_5_slownik import dictionary

dictionary = {"imie": "Radek", 'nazwisko': "Kowalski"}

# wypisze klucze
for i in dictionary:
    print(i)
# imie
# nazwisko

for i in dictionary.keys():
    print(i)
# imie
# nazwisko

# wypisanie wartosci
for i in dictionary.values():
    print(i)
# Radek
# Kowalski

# wypisanie par
for i in dictionary.items():
    print(i)
# ('imie', 'Radek')
# ('nazwisko', 'Kowalski')
# imie <==> Radek
# nazwisko <==> Kowalski
for k, v in dictionary.items():
    print(k, "<==>", v)
