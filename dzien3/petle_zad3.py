# while - pętla sterowana warunkiem

# pętla nieskończona
# while True:
#     print("Komunikat")
#
licznik = 0

while True:
    licznik += 1  # licznik = licznik + 1
    print("Komunikat 2 !!")
    if licznik > 10:
        break  # przerywanie pętli

print(licznik)  # 11

licznik = 0
while licznik < 10:
    licznik += 1
    print("Komunikat 3")

# kalkulator

# while True:
#     print(f"""
# 1. Dodawanie
# 5. Koniec""")
#     odp = input("Wybierz opcje menu: ")
#
#     if odp == "5":
#         break
#
#     a = int(input("Liczba a:"))
#     b = int(input("Liczba b:"))
#
#     if odp == "1":
#         print(a + b)
#     else:
#         print("nie ma")

my_list = [1, 5, 2, 5, 90, 3, 5, 6, 7, 91]

while 5 in my_list:
    my_list.remove(5)
print(my_list)  # [1, 2, 90, 3, 6, 7, 91]

my_list = [1, 5, 2, 5, 90, 3, 5, 6, 7, 91]

print(dict.fromkeys(my_list))
# {1: None, 5: None, 2: None, 90: None, 3: None, 6: None, 7: None, 91: None}

print(list(dict.fromkeys(my_list)))  # [1, 5, 2, 90, 3, 6, 7, 91], zachowana kolejność
