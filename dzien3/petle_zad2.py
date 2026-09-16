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

for k, v in dictionary.items():
    print(k, v, sep="<==>")
# imie<==>Radek
# nazwisko<==>Kowalski

pol_ang = {'pies': 'dog', "kot": "cat", "dach": "roof"}

ang_pol = {}  # pusty słownik
for k, v in pol_ang.items():
    ang_pol[v] = k

print(ang_pol)  # {'dog': 'pies', 'cat': 'kot', 'roof': 'dach'}

print({v: k for k, v in pol_ang.items()})
# {'dog': 'pies', 'cat': 'kot', 'roof': 'dach'}
