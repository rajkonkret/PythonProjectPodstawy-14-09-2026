# zbior (set) - przechowuje unikalne wartosci
# nie zachowuje kolejnosci
# nie posiada indeksu

lista = [44, 55, 66, 777, 33, 22, 11, 33, 11, 777]
zbior = set(lista)  # rzutowanie na zbiór
print(type(zbior))  # <class 'set'>
print(zbior)  # {33, 66, 777, 11, 44, 22, 55}

# pusty zbior
zb2 = set()  # tylko za pomocą słowka set
print(zb2)  # set()

# dodawanie elementu do zbioru
zbior.add(33)
zbior.add(33)
zbior.add(33)
zbior.add(33)
zbior.add(33)
zbior.add(33)
zbior.add(18)
zbior.add(33)
zbior.add(18)
zbior.add(33)
zbior.add(54)
zbior.add(33)
zbior.add(25)

print(zbior)
# {33, 66, 777, 11, 44, 18, 22, 55, 54, 25}

# usunięcie elementu
zbior.remove(55)
print(zbior)  # {33, 66, 777, 11, 44, 18, 22, 54, 25}

# pop() - usunie pierwszy element
print(zbior.pop())  # 33
print(zbior)  # {66, 777, 11, 44, 18, 22, 54, 25}

# operacje na zbiorach
zbior_2 = {667, 11, 14, 44, 12.34, 18, 52, 667, 62, 99}

# suma zbiorów - tworzy nowy zbior
print(zbior | zbior_2)  # {66, 99, 777, 11, 44, 12.34, 14, 18, 52, 22, 54, 25, 667, 62}
print(zbior.union(zbior_2))  # {66, 99, 777, 11, 44, 12.34, 14, 18, 52, 22, 54, 25, 667, 62}

# częśc wspólna
print(zbior & zbior_2)  # {18, 11, 44}
print(zbior.intersection(zbior_2))  # {18, 11, 44}

# różnica
print(zbior - zbior_2)  # {66, 777, 54, 22, 25}
print(zbior.difference(zbior_2))  # {66, 777, 54, 22, 25}
print(zbior_2.difference(zbior))  # {99, 12.34, 14, 52, 667, 62}

# łaczy zbiór, zmienia bazowy
zbior.update(zbior_2)
print(zbior)  # {66, 777, 11, 12.34, 14, 18, 22, 25, 667, 99, 44, 52, 54, 62} zmiana oryginalnej kolekcji

# difference_update(zbior_2)

krotka = tuple(zbior)
print(krotka)
# (66, 777, 11, 12.34, 14, 18, 22, 25, 667, 99, 44, 52, 54, 62)

lista = list(zbior)
print(lista)
# [66, 777, 11, 12.34, 14, 18, 22, 25, 667, 99, 44, 52, 54, 62]

# in - sprawdzanie czy element istnieje w kolekcji

# zbior jest hashowany, najszybsze wyszukiwanie
print(667 in zbior)  # True
print(777 in lista)  # True
print(667 in krotka)  # True

print("radek" in zbior_2)  # False
