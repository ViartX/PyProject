# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна
# корректно обработать эту ситуацию и не завершиться с ошибкой.

class DivByZero(Exception):
    def __init__(self, txt):
        self.txt = txt

while True:
    inp_data = input("Введите делимое (q для выхода): ")
    if inp_data == "q":
        break
    try:
        delimoe = int(inp_data)
    except ValueError:
        print("Вы ввели не число")
        continue

    inp_data = input("Введите делитель (q для выхода): ")
    if inp_data == "q":
        break
    try:
        delitel = int(inp_data)
    except ValueError:
        print("Вы ввели не число")
        continue

    try:
        if (delitel == 0):
            raise DivByZero("Деление на ноль запрещено")
    except DivByZero as err:
        print(err)
        continue

    print(f"Результат: {delimoe/delitel}")