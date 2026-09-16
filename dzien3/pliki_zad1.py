# działania z plikami
# filehandler

# context manager
# with - context manager w pythonie

# https://docs.python.org/3.14/builtins/functions.html#open
with open('test.log', "w", encoding='utf-8') as file:
    file.write("Powitanie\n")
    file.write("Jeszcze jedno\n")

# FileExistsError: [Errno 17] File exists: 'test.log'
# with open("test.log", "x", encoding='utf-8') as file:
#     file.write("TestX")

# dopisanie do pliku, na końcu
with open('test.log', "a", encoding='utf-8') as file:
    file.write("Powitanie\n")
    file.write("Jeszcze jedno\n")
    file.write("Dośdane\n")

with open("test.log", "r", encoding='utf-8') as f:
    lines =f.read()

print(lines)
# chardet