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
