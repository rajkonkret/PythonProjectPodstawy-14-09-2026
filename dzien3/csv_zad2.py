# pandas - analiza danych
import pandas

# pip install pandas

data = pandas.read_csv('records_dict.csv')
print(data)

#     name branch  year  cgpa
# 0  radek    coe     3     0

# csv.Sniff() - wykrywanie delimitera
data = pandas.read_csv("records_dict_list.csv", delimiter=";")
print(data)
#     name branch  year  cgpa
# 0  radek    coe     3     0
# 1  radek    coe     3     0
# 2  radek    coe     3     0
# 3  radek    coe     3     0

print(data.columns)
# Index(['name', 'branch', 'year', 'cgpa'], dtype='str')