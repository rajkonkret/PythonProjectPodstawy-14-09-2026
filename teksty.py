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

# slicowanie
print(tekst[3:]) # "aj Świecie" do ostatniego włacznie