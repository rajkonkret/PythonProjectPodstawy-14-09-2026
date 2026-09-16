# Kowalski,Jan,Kłodzko
# Nowak,Zenon,Szczecin
# Brzęczyszczykiewicz,Grzegorz,Chrząszczyżewoszyce
# csv - dane oddzielone znakiem podziału ,tab;" "|
import csv

row = ['radek', 'coe', "3", 0]

filename = 'records.csv'

with open(filename, "w") as csv_f:
    csv_writer = csv.writer(csv_f)
    csv_writer.writerow(row)

