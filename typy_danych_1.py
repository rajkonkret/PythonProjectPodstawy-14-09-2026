wiek = 47  # int
rok = 2026  # int
temp = 36.6  # float

print(wiek + rok)
print(wiek - rok)
print(wiek * rok)
print(wiek / rok)  # 0.02319842053307009 float
print(rok // wiek)  # część całkowita dzieleniea 43
print(rok % wiek)  # reszta z dzielenia 5, modulo

print(10 % 3)  # 1

print(wiek ** rok)  # potęgowanie

print(len(str(wiek ** rok)))  # 3388
# print(len(str(wiek ** rok ** 2)))
# ValueError: Exceeds the limit (4300 digits) for integer string conversion;
# use sys.set_int_max_str_digits() to increase the limit

print(54 - 5 * 43 + 4 / 2 + 4 / 2)  # -157.0
print(54 - 5 * 43 + 4 / (2 + 4 / 2))  # -160.0
