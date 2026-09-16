# funkcja - blok programu, który można wykonać wielokrotnie
# funkcja musi byc najpierw zadeklarowana
# żeby funkcja się uruchomiła musi zostać wywołana

a = 6
b = 8


# deklaracja funkcji
def dodaj():
    print(a + b)


def dodaj2(a, b):
    print(a + b)


def dodaj3(a, b, c=0):  # wartość domyslna
    print(a + b + c)


# wywołanie funkcji
dodaj()  # 14

# dodaj2() # TypeError: dodaj2() missing 2 required positional arguments: 'a' and 'b'
dodaj2(5, 9)  # 14

# argumenty pozycyjne
dodaj3(2, 5)  # 7
dodaj3(2, 5, 10)  # 17

# argumenty po nazwie
dodaj3(c=100, b=90, a=9)  # 199

# mieszane
dodaj3(1, c=34, b=99)  # 134

# dodaj3(a=90, 3, 4) # SyntaxError: positional argument follows keyword argument
print(50 * "-")
wyn = dodaj3(1, 2, 3)
print(wyn)


# 6
# None

# funkcje zwracające wynik
def odejmij(a=0, b=0, c=0):
    return a - b - c  # zwraca wynik
    # return a, b, c # zwraca krotke


print(odejmij(1, 2, 3))  # -4
wyn = odejmij(5, 90)
print(wyn)  # -85

# funkcja lambda
# skrócony zapis funkcji
# zwraca wynik

odejmij4 = lambda a, b, c=0: a - b - c
wyn = odejmij4(4, 9)
print(wyn)  # -5

# funkcja anonimowa
lista = [6, 9, 10, 11]

# mapowanie danych
l1 = []
for i in lista:
    l1.append(i * 1.1)
print(l1)  # [6.6000000000000005, 9.9, 11.0, 12.100000000000001]

print([i * 1.1 for i in lista])  # [6.6000000000000005, 9.9, 11.0, 12.100000000000001]

# map(), filter(), reduce()
# funkcje wyższego rzędu - jako argument przyjmują inną funkcję
# lambda jako funkcja anonimowa - użycie w miejscu deklaracji
print(f"Użycie map(): {list(map(lambda x: x * 1.1, lista))}")
# Użycie map(): [6.6000000000000005, 9.9, 11.0, 12.100000000000001]

print(f"Użycie filter(): {list(filter(lambda x: x > 9, lista))}")
# Użycie filter(): [10, 11]