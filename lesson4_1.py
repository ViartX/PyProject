# функция принимает параметры: выработка в часах, часовая ставка, премия
from sys import argv

script_name, hourly_payment, worked_hours, incentive = argv

print("Часовая ставка: ", hourly_payment)
print("Отработано часов: ", worked_hours)
print("Премия: ", incentive)
print("Оплата: ", (float(hourly_payment) * float(worked_hours)) + float(incentive))