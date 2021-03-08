# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
#
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.


import json


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


r_dict_profit = {}
r_dict_average_profit = {}
i_profit_sum = 0
n_profit_companies = 0

with open("lesson5_7_1.txt") as f_text_in:
    for line in f_text_in:
        company_name = get_string_piece(line, " ", 0)
        company_revenue = get_valid_num(get_string_piece(line, " ", 2).strip(" "))
        company_spends = get_valid_num(get_string_piece(line, " ", 3).strip(" "))
        company_profit = company_revenue - company_spends
        if company_profit > 0:
            r_dict_profit[company_name] = company_profit
            i_profit_sum += company_profit
            n_profit_companies += 1

f_text_in.close()
if n_profit_companies > 0:
    r_dict_average_profit["Средняя прибыль"] = i_profit_sum / n_profit_companies
else:
    r_dict_average_profit["Средняя прибыль"] = "Нет прибыльных компаний"

total_list = []
total_list.append(r_dict_profit)
total_list.append(r_dict_average_profit)

with open("lesson5_7_2.json", "w") as json_file:
    json.dump(total_list, json_file, ensure_ascii=False)

print(total_list)

