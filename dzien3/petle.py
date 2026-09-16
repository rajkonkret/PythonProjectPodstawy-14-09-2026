# pętle - możliwośc wykonania kodu wilokrotnie
# for - pętla iteracyjna

for i in range(5):  # od 0 do 4
    print(i)
# 0
# 1
# 2
# 3
# 4

for i in range(30):  # o d0 do 29
    pass  # nic nie rób

print(i)  # 29

for _ in range(15):  # niema zmiennna
    print("Tesst podłoga")

print(_)  # 14

for i in range(10):
    if i % 2 == 0:  # module, reszta z dzielenia
        print(i, "parzysta")
# 0 parzysta
# 2 parzysta
# 4 parzysta
# 6 parzysta
# 8 parzysta

lista3 = []
# parzyste dodac do listy
for i in range(10):
    if i % 2 == 0:
        lista3.append(i)

print(lista3)  # [0, 2, 4, 6, 8]

# list comprehensions
lista3 = [j for j in range(10) if j % 2 == 0]
print(lista3)  # [0, 2, 4, 6, 8]

# kolejne elementy listy
for i in range(len(lista3)):
    print(lista3[i])

for c in lista3:
    print(c)
# 0
# 2
# 4
# 6
# 8


imiona = ['Sylwia', 'Marek', "Tomek", 'Anna']

for o in imiona:
    print(o)
# Sylwia
# Marek
# Tomek
# Anna

# 0 Sylwia
for o in imiona:
    print(imiona.index(o), o)
# 0 Sylwia
# 1 Marek
# 2 Tomek
# 3 Anna

# enumerate()
for p in enumerate(imiona):
    print(p)
    # (0, 'Sylwia')
    # (1, 'Marek')
    # (2, 'Tomek')
    # (3, 'Anna') -> 0 Anna

for i, o in enumerate(imiona):
    print(i, o)
# 0 Sylwia
# 1 Marek
# 2 Tomek
# 3 Anna

imiona = ['Sylwia', 'Marek', "Tomek", 'Anna']
wiek = [34, 43, 23, 19]

# Sylwia 34
for o in imiona:
    print(imiona.index(o), wiek[imiona.index(o)])

imiona = ['Sylwia', 'Marek', "Tomek", 'Anna', "Kamila"]
wiek = [34, 43, 23, 19]

# zip() - łączenie kolekcji
for i in zip(imiona, wiek):
    print(i)
# ('Sylwia', 34)
# ('Marek', 43)
# ('Tomek', 23)
# ('Anna', 19)

for i, w in zip(imiona, wiek):
    print(i, w)
# Sylwia 34
# Marek 43
# Tomek 23
# Anna 19

for i in enumerate(zip(imiona, wiek)):
    print(i)
# (0, ('Sylwia', 34))
# (1, ('Marek', 43))
# (2, ('Tomek', 23))
# (3, ('Anna', 19)) -> 3 Anna 19

for i, (o, w) in enumerate(zip(imiona, wiek)):
    print(i, o, w)
# 0 Sylwia 34
# 1 Marek 43
# 2 Tomek 23
# 3 Anna 19