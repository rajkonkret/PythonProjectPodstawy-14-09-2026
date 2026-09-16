# klasa - przepis, template
# obiekt - zbudowany wg klasy
# hermetyzacja, dziedziczenie, polimorfizm, abstrakcja

# CamelCase
class Human:
    """
    Klasa Human
    """

    def __init__(self, imie, wiek, plec="k"):
        """
        Metoda inicjalizujące
        :param imie:
        :param wiek:
        :param plec:
        """
        self.imie = imie
        self.wiek = wiek
        self.plec = plec

    def wypisz_wiek(self):
        print(f"Mam na imię: {self.imie}")


print(Human.__doc__)
# Klasa Human
cz1 = Human("Radek", 60, "m")
print(cz1.imie)  # Radek
print(cz1.wiek)  # 60
print(cz1.plec)  # m

cz1.wypisz_wiek() # Mam na imię: Radek

cz2 = Human("Anna", 45)
print(cz2.imie)
print(cz2.wiek)
print(cz2.plec)
cz2.wypisz_wiek()
# Anna
# 45
# k
# Mam na imię: Anna