# pep8
# https://peps.python.org/pep-0008/

print('Hello World')
print()
print("Hello World")
# Hello World
#
# Hello World

print("Nazywam się Radek")

# ctrl / - komentarz
# print('Radek")

#   File "C:\Users\CSComarch\PycharmProjects\PythonProjectPodstawy-14-09-2026\pierwszy.py", line 13
#     print('Radek")
#           ^
# SyntaxError: unterminated string literal (detected at line 13)
#
# Process finished with exit code 1

print("Dalszy ciąg programu")
# ctrl alt l - formatowanie kodu

print(type("Radek"))  # <class 'str'> - tekstowy

print("39")
print(type("39"))
print("39" + "14")  # 3914 łaczenie tekstów , konkatenacja

print(39)
print(type(39))  # <class 'int'> - liczby calkowite

print(39 + 14)  # 53

# rzutowanie
print(type(int("39")))  # <class 'int'>
print(int("39") + int("56"))  # 95

print("Radek_" + str(1))  # Radek_1

# print(int("A")) # ValueError: invalid literal for int() with base 10: 'A'

print(5 * "4")  # 44444
print(5 * 4)  # 20

# zmienna - pudełko na dane
# typowanie dynamiczne

name = "Radek"
print(name)  # Radek
print(type(name))  # <class 'str'>

name = 67
print(name)
print(type(name))
# 67
# <class 'int'>

