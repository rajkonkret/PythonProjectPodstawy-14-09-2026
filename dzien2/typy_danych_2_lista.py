# kolekcje

# lista - przechowuje dowolną ilość danych, różnego typu na raz
# zachowuje kolejnośc przy dodawaniu elementów

# pusta lista
lista = []
print(lista)  # []
print(type(lista))  # <class 'list'>

pusta_lista = list()
print(pusta_lista)  # []
print(type(pusta_lista))  # <class 'list'>

# dodanie elementów do listy
lista.append("Radek")
lista.append("Tomek")
lista.append("Zenek")
lista.append("Grzegorz")
lista.append("Anna")
lista.append("Karolina")
print(lista)
# ['Radek', 'Tomek', 'Zenek', 'Grzegorz', 'Anna', 'Karolina']

# długość
print(len(lista))  # 6

# ['Radek', 'Tomek', 'Zenek', 'Grzegorz', 'Anna', 'Karolina']
#     0        1        2         3          4        5

print(lista[1])
print(lista[3])
print(lista[5])
# Tomek
# Grzegorz
# Karolina

# print(lista[10])  # IndexError: list index out of range

# ostatni element
print(lista[5])  # Karolina
print(lista[len(lista) - 1])  # Karolina
print(lista[-1])  # Karolina
print(lista[-2])  # Anna
print(lista[-4])  # Zenek

# slicowanie
print(lista[0:3])  # 012, ['Radek', 'Tomek', 'Zenek']
print(lista[:3])  # ['Radek', 'Tomek', 'Zenek']

print(lista[2:])  # ['Zenek', 'Grzegorz', 'Anna', 'Karolina'], z ostatnim włącznie
print(lista[2:5])  # ['Zenek', 'Grzegorz', 'Anna'], bez ostatniego

print(lista[2:10])  # ['Zenek', 'Grzegorz', 'Anna', 'Karolina']
print(lista[12:26])  # []

print(lista[:])  # ['Radek', 'Tomek', 'Zenek', 'Grzegorz', 'Anna', 'Karolina']

# ['Radek', 'Tomek', 'Zenek', 'Grzegorz', 'Anna', 'Karolina']
#     0        1        2         3          4        5
#     -6       -5       -4        -3         -2       -1
print(lista[-2:0])  # [] -> [4:0]
print(lista[0:-2])  # ['Radek', 'Tomek', 'Zenek', 'Grzegorz']

# od 0 do 14
lista_15 = list(range(15))  # 15 elementów od 0 do 14
print(lista_15)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

print(lista_15[::2])  # [start:stop:krok], [0, 2, 4, 6, 8, 10, 12, 14]
print(lista_15[::3])  # [0, 3, 6, 9, 12]

print(lista_15[::-1])
# [14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

print(lista[-2:0:-1])  # ['Anna', 'Grzegorz', 'Zenek', 'Tomek']

tablica = [[1, 2], [3, 4]]
# numpy - tablice/macierze, pandas

print(lista)
# ['Radek', 'Tomek', 'Zenek', 'Grzegorz', 'Anna', 'Karolina']
