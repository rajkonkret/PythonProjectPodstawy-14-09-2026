tekst = "Witaj Świecie"

print(type(tekst))
print(tekst)
# <class 'str'>
# Witaj Świecie

tekst.upper()
print(tekst)  # Witaj Świecie

# teksty są niemutowalne
# Return a copy of the string converted to uppercase.
# pula tekstów
print(tekst.upper())  # WITAJ ŚWIECIE
tekst_upper = tekst.upper()
print(tekst_upper)  # WITAJ ŚWIECIE

print(tekst.lower())  # witaj świecie

print(tekst.title())  # Witaj Świecie
print(tekst.capitalize())  # Witaj świecie

# Witaj Świecie
# 01234567890..

# ctrl d - powielanie
print(tekst[1])  # i
print(tekst[3])  # a
print(tekst[6])  # Ś

print(tekst.index("Ś"))  # 6
print(tekst.index("e"))  # 9, pierwsza od lewej

print(tekst.count("e"))  # wystepuje 2 razy

print(len(tekst))  # długość 13 znaków

print(tekst.count("j", 0, 4))  # od pierwszego do czwartego -> 0123, z prawej niewłącznie

print(tekst.removesuffix("Świecie"))  # "Witaj "

# strip() - usuwanie białych znaków, wiodących, kończących spacji
print(tekst.removesuffix("Świecie").strip())  # "Witaj"

# slicowanie Witaj Świecie
print(tekst[3:])  # "aj Świecie" do ostatniego włacznie

imie = "Radek"

# Mam na imię: ...
print("Mam na imię:" + str(imie))  # Mam na imię:Radek
print('Mam na imie:', imie)  # Mam na imie: Radek
# sep
# string inserted between values, default a space.
# end
# string appended after the last value, default a newline.

print("Mam na imię", imie, sep="ooo")  # Mam na imięoooRadek

# f-string, wstrzykiwanie wartości zmiennej do tekstu
tekst_format = f"Mam na imię {imie}."
print(tekst_format)  # Mam na imię Radek.

tekst_format = f"\tMam na imię {imie}.\n i lubię pythona.\b"
print(tekst_format)
# \t - tabulator
# \n - nowa linia
# \b - backspace

#  	Mam na imię Radek.
#  i lubię pythona

starszy = "Witaj %s"  # %s - string
print(starszy % imie)  # Witaj Radek
