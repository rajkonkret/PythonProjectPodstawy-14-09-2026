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


