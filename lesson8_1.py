# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год». В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа,
# месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

class Date:

    monthly_max = (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

    def __init__(self, date_string):
        self.date_string = date_string

    @classmethod
    def get_ddmmyy(cls, date_string: str):
        order_tuple = ("день", "месяц", "год")
        string_list = date_string.split("-")
        int_list = []
        for i in range(0, len(string_list)):
            int_list.append(int(string_list[i]))
            print(f"{order_tuple[i]}: {int_list[i]}")
        return int_list


    # проверка на високосный год(век) не осуществляется, в феврале макисмум 29 дней
    @staticmethod
    def is_valid_date(date_string: str):
        local_date = Date(date_string)
        date_list = local_date.get_ddmmyy(date_string)
        print(date_list)
        if not(1 <= date_list[1] <= 12):
            print(f"в строке {date_string} неверно указан месяц")
            return False
        if date_list[0] < 1:
            print(f"в строке {date_string} день месяца не может быть меньше 1")
            return False
        if date_list[0] > Date(date_string).monthly_max[date_list[1]]:
            print(f"в строке {date_string} слишком много дней в месяце")
            return False
        return True




data = Date("11-05-1983")
#print(Date.get_ddmmyy("12-05-2017"))
print(Date.is_valid_date("32-01-2017"))