# итератор, работающий по списку
# пример вызова python.exe C:/ARTEM/PyProject/lesson4_62.py 10
# параметр 2 - число итераций

from itertools import count
from sys import argv
from itertools import cycle

script_name, iteration_num = argv

list1 = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
iter = cycle(list1)
i = 0

while i < int(iteration_num):
    print(next(iter))
    i += 1

