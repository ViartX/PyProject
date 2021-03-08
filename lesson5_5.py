# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

import random

numbers_sum = 0
f_text = open("lesson5_5.txt", 'w')

for i in range(1, 101):
    new_number = random.randint(1, 101)
    f_text.write(str(new_number) + " ")
    numbers_sum += new_number

f_text.close()
print(f"Сумма чисел в файле равна {numbers_sum}")