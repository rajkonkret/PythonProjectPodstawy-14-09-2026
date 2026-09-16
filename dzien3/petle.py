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

