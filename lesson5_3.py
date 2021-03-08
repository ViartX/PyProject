# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.


employees_number = 0
sum_salary = 0

f_text = open("lesson5_3.txt", 'r')

for line in f_text:
    list_line = line.split()
    salary = int(list_line[1])
    if salary < 20000:
        print(list_line[0])
    sum_salary += salary
    employees_number += 1

print(f'Средняя зарплата в трансгалактической корпорации "Колокольчик": {sum_salary/employees_number} руб.')