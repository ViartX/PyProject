""" Функция для выполнения операции деления. """


def f_division(delimoe, delitel):
    if delitel == 0:
        return None
    return delimoe/delitel


""" Функция для вывода данных о пользователе. """


def f_user_data(first_name, last_name, birth_year, city, email):
    return (f"Mr./Mrs. {first_name} {last_name} born in {birth_year} from {city}. Write him/her at {email}")


""" Функция принимает три аргумента и возвращает сумму двух наибольших."""


def f_sum_of_two(arg1, arg2, arg3):
    arg_list = [arg1, arg2, arg3]
    arg_list.sort()
    return arg_list[1] + arg_list[2]


""" Функция принимает два аргумента a и b, возводит а в степень b.

    Известно, что b<0     """


def f_minus_power(a, b):
    if a <= 0:
        return None
    if b >= 0:
        return None
    result = 1.0
    for i in range(0, abs(b)):
        result = result / a

    return result


""" Функция принимает слово, первую букву преобразует в большую."""


def f_int(arg):
    if len(arg) == 0:
        return "no value in string"
    elif len(arg) == 1:
        return arg[0].upper()
    else:
        return arg[0].upper() + arg[1:]


# Деление с использованием функции
print("Деление с использованием функции")
value1 = int(input(f"Введите делимое : "))
value2 = int(input(f"введите делитель : "))
print(f"Результат : {f_division(value1, value2)}")
print()

# Вывод данных о пользователе
print("Вывод данных о пользователе")
print(f_user_data(first_name="Ivan", last_name="Petrov", birth_year="2000", city="Boston", email="Ivan.Petrov@www.ru"))
print()

# Вызов функции трех аргументов
print("Вызов функции трех аргументов")
value1 = int(input(f"Введите аргумент 1 : "))
value2 = int(input(f"Введите аргумент 2 : "))
value3 = int(input(f"Введите аргумент 3 : "))
print(f"Результат : {f_sum_of_two(value1, value2, value3)}")
print()

# возведение в степень
print("возведение в степень")
value1 = float(input(f"Введите вещественное положительное число : "))
value2 = int(input(f"Введите целое отрицательное число : "))
print(f"Результат : {f_minus_power(value1, value2)}")
print()

# суммирование введенных чисел
sum = 0
is_exit = False
while True:
    if is_exit: break
    str = input(f'Введите сроку чисел, q - для выхода, текущая сумма {sum} : ')
    values_list = str.split()
    for i in range(0, len(values_list)):
        if values_list[i] == 'q':
            is_exit = True
            break
        elif values_list[i].isdigit():
            try:
                value = float(values_list[i])
                sum += value
            except ValueError:
                continue

print(f"Результат : {sum}")
print()

# первая буква - большая
str = input('Введите строку из слов, разделенных пробелами: ')
str_list = str.split()
str_result = ""
for i in range(0, len(str_list)):
    str_result += f_int(str_list[i]) + " "

str_result = str_result[0: -1] # убираем последний пробел
print(f"Результат : {str_result}")
print()

