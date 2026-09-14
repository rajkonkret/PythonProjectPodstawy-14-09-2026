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

# float - błąd zaokrąglenia
print(0.2 + 0.8)  # 1.0
print(0.2 + 0.7)  # 0.8999999999999999
# For example, in a floating-point arithmetic with five base-ten digits,
# the sum 12.345 + 1.0001 = 13.3451 might be rounded to 13.345
# decimal - pozwala bezpiecznie pracowac z zaokrągleniami