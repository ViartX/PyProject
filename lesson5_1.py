# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.


f_text = open("lesson5_1.txt", 'w')
while True:
    new_line = input("Введите строку в файл, для выхода - пустую строку: ")
    if new_line == "":
        break
    f_text.write(new_line + "\n")
f_text.close()

