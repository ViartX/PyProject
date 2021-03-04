# итератор, генерирующий целые числа, начиная с указанного
# пример вызова python.exe C:/ARTEM/PyProject/lesson4_61.py 3 10
# параметр 2 - от какого числа итерировать, параметр 3 - до какого


from itertools import count
from sys import argv


script_name, first_number, last_number = argv
first_number = int(first_number)
last_number = int(last_number)

if first_number <= last_number:
    for el in count(first_number):
        if el > last_number:
            break
        else:
            print(el)
else:
    for el in count(first_number, -1):
        if el < last_number:
            break
        else:
            print(el)

