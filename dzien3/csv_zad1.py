# Kowalski,Jan,Kłodzko
# Nowak,Zenon,Szczecin
# Brzęczyszczykiewicz,Grzegorz,Chrząszczyżewoszyce
# csv - dane oddzielone znakiem podziału ,tab;" "|
import csv

row = ['radek', 'coe', "3", 0]
fields = ['name', 'branch', "year", 'cgpa']

filename = 'records.csv'

# newline="" - ominiecie problemu pustych na linii
with open(filename, "w", newline="") as csv_f:
    csv_writer = csv.writer(csv_f)
    csv_writer.writerow(fields)
    csv_writer.writerow(row)

dict_name = dict(zip(fields, row))
print(dict_name)
# {'name': 'radek', 'branch': 'coe', 'year': '3', 'cgpa': 0}

filename = 'records_dict.csv'
with open(filename, "w", newline="") as csv_f:
    csv_writer = csv.DictWriter(csv_f, fieldnames=fields)
    csv_writer.writeheader()
    csv_writer.writerow(dict_name)