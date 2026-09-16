import matplotlib.pyplot as plt


miesiace = ["Styczen", "Luty", "Marzec", "Kwiecien", "Maj", "Czerwiec"]
sprzedaz = [12, 18, 15, 24, 29, 35]

plt.figure(figsize=(9, 5))
plt.plot(
    miesiace,
    sprzedaz,
    marker="o",
    color="royalblue",
    linewidth=2,
    label="Sprzedaz",
)

plt.title("Sprzedaz w pierwszej polowie roku")
plt.xlabel("Miesiac")
plt.ylabel("Liczba sprzedanych sztuk")
plt.grid(True, linestyle="--", alpha=0.5)
plt.legend()
plt.tight_layout()

plt.savefig("wykres_sprzedazy.png", dpi=150)
plt.show()
