# słownik - para klucz:wartosc
# {"user":"Radek"}
# klucze nie mogą się powtarzac
# {
#   "name": "John",
#   "age": 30,
#   "city": null -> None
# }
# słownik jest odpowiednikiem json

# pusty słownik
dictionary = {}
print(dictionary)  # {}
print(type(dictionary))  # <class 'dict'>

dictionary_1 = dict()
print(dictionary_1)  # {}
print(type(dictionary_1))  # <class 'dict'>

# dodawanie eleemntów do słownika
dictionary['imie'] = "Radek"
print(dictionary)  # {'imie': 'Radek'}

# dodać klucz 'wiek'
dictionary['wiek'] = 53
print(dictionary)  # {'imie': 'Radek', 'wiek': 53}

print(dictionary.keys())
print(dictionary.values())
print(dictionary.items())

# dict_keys(['imie', 'wiek'])
# dict_values(['Radek', 53])
# dict_items([('imie', 'Radek'), ('wiek', 53)])

# nadapisanie
dictionary['imie'] = "Tomek"
print(dictionary)  # {'imie': 'Tomek', 'wiek': 53}

dictionary['imie'] = ['Radek', "Tomek", "Magda"]
print(dictionary)
# {'imie': ['Radek', 'Tomek', 'Magda'], 'wiek': 53}

# wypisywanie
print(dictionary['wiek'])  # 53

# wypisac 'Tomek'
print(dictionary['imie'])  # ['Radek', 'Tomek', 'Magda']
print(dictionary['imie'][1])  # Tomek
print(dictionary['imie'][1].upper())  # TOMEK
print(dictionary['imie'][::-1])  # ['Magda', 'Tomek', 'Radek']

# print(dictionary['Imie'])  # KeyError: 'Imie'

print(dictionary.get("Imie"))  # None
print(dictionary.get("Imie", "default"))  # default

dictionary.update({"date": "12-12-2040"})
print(dictionary)
# {'imie': ['Radek', 'Tomek', 'Magda'], 'wiek': 53, 'date': '12-12-2040'}

dict_small = {'x': 20}
dict_small.update([("y", 30), ("z", "50")])
print(dict_small)  # {'x': 20, 'y': 30, 'z': '50'}

# input() - mozliwosc wprowadzania dancyh

# tekst = input("Podaj imię: ")
# print(tekst)
# Podaj imię: Radek
# Radek

# napisac aplikacje kalkulator
# input() zwraca str
a = int(input("Podaj wartość a: "))
b = input("Podaj wartość b: ")
print(int(a) + float(b))
# Podaj wartość a: 8
# Podaj wartość b: 9
# 17.0
