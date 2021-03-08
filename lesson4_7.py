# Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор.
# Функция должна вызываться следующим образом: for el in fact(n).
# Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел,
# начиная с 1! и до n!.
# пример вызова python.exe C:/ARTEM/PyProject/lesson4_7.py 6
# параметр 2 - число, для кторого считаем факториал

from sys import argv


def generator():
    value = 1
    el = 1
    while True:
        value = value * el
        el += 1
        print(value)
        yield el


script_name, fact_number = argv

g = generator()
for el in g:
    if el > int(fact_number):
        break
