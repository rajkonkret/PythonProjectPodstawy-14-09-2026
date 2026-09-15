# krotka - kolekcja niemutowalna (tylko do odczytu)
# pozwala efektywniej zarzadzać pamięcią

tupla_imiona = "Zenek", "Tomek", "Marek", "Ania"
print(type(tupla_imiona))
print(tupla_imiona)  # <class 'tuple'>
# ('Zenek', 'Tomek', 'Marek', 'Ania')

# tupla_liczby = 43, 45, 22.34, 11, 200
tupla_liczby = (43, 45, 22.34, 11, 200)
print(type(tupla_liczby))  # <class 'tuple'>
print(tupla_liczby)  # (43, 45, 22.34, 11, 200)

# tupla jednoelementowa
tupla_jeden = (45,)  # pep8 zaleca nawias dla tupli jednoelemntowych
print(type(tupla_jeden))  # <class 'tuple'>

tupla_dwa = tuple('45')
print(tupla_dwa)
# <class 'tuple'>
# ('4', '5')

# tupla_jeden[0] = 123
# TypeError: 'tuple' object does not support item assignment
del tupla_jeden
# print(tupla_jeden) # NameError: name 'tupla_jeden' is not defined

print(tupla_imiona)
print(tupla_imiona.index("Zenek"))
print(tupla_imiona.count("Zenek"))

print(len(tupla_imiona))  # długosc 4

tup = 1, 2

# a - pierwszy element
# b - drugi element

a = tup[0]
b = tup[1]
print(a)
print(b)

# rozpakowanie krotki
a, b = tup
print(a, b)  # 1 2

# zamiana wartości miejscami
a, b = b, a
print(a, b)  # 2 1

print(tupla_imiona)  # ('Zenek', 'Tomek', 'Marek', 'Ania')
print(len(tupla_imiona))  # 4

# name1, name2, name3
# name1, name2, name3 = tupla_imiona
# ValueError: too many values to unpack (expected 3, got 4)

# * dowolna ilosc elementów
# worek na pozostałe dane
name1, name2, *name3 = tupla_imiona
print(name1, name2, name3)
# Zenek Tomek ['Marek', 'Ania']

name1, *name2, name3 = tupla_imiona
print(name1, name2, name3)  # Zenek ['Tomek', 'Marek'] Ania

*name1, name2, name3 = tupla_imiona
print(name1, name2, name3)  # ['Zenek', 'Tomek'] Marek Ania
