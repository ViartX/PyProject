# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.


numbers = {"One" : "Один", "Two" : "Два", "Three" : "Три", "Four" : "Четыре", "Five" : "Пять"}

f_text_in = open("lesson5_4_1.txt", 'r')
f_text_out = open("lesson5_4_2.txt", 'w')

for line in f_text_in:
    list_line = line.split()
    number = (list_line[0])
    list_line[0] = numbers[number]
    # f_text_out.write(''.join(list_line) + "\n")
    f_text_out.write(f"{numbers[number]} {list_line[1]} {list_line[2]}\n")

f_text_in.close()
f_text_out.close()