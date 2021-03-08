# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет
# и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.
#
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
#
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

# функция получает на вход строку, разделитель и номер элемента
# ищет в строке подстроку под номером position, разделенную подстрокой divider
def get_string_piece(string: str, divider: str, position: int):
    l_list = string.split(divider)
    if position >= len(l_list):
        return ""
    else:
        return l_list[position]


# функция получает на вход строку, возвращает первое корректное число
# строка 10А -> вернет 10
# строка d10 -> вернет 0
def get_valid_num(string: str):
    value = ""
    for i in range(0,len(string)):
        if string[i].isdigit():
            value = value + string[i]
        else:
            break
    if value == "":
        return 0
    else:
        return int(value)


f_text_in = open("lesson5_6.txt", 'r')
r_dict = {}

for line in f_text_in:
    s_subject = get_string_piece(line, ":", 0)
    s_hours = get_string_piece(line, ":", 1)
    s_hours = s_hours.strip(" ")
    i_hours_sum = 0
    i = 0
    while True:
        s_hour = get_string_piece(s_hours, " ", i)
        if s_hour == "":
            break
        else:
            i_hour = get_valid_num(s_hour)
        i_hours_sum += i_hour
        i += 1
    r_dict[s_subject] = i_hours_sum

print(r_dict)
f_text_in.close()
