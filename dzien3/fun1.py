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