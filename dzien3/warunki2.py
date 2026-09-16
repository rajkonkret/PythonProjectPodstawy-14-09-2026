# od pythona 3.10
# match case

lista = []

lang = input("Podaj znany Ci język programowania: ")

match lang:
    case "python":
        lista.append("Znam Pythona")
    case "java":
        lista.append("Znam Javę")
    case _:  # wartość domyślna
        print("Nie znam takiego języka")

print(lista)
# Podaj znany Ci język programowania: java
# ['Znam Javę']
