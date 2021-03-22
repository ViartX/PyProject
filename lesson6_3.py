# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода
# с учетом премии (get_total_income).
# Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).


class Worker:
    name: str
    surname: str
    position: str
    _income = {}

    def __init__(self, new_name, new_surname, new_position, new_income):
        self.name = new_name
        self.surname = new_surname
        self.position = new_position
        self._income = new_income

    def get_income(self):
        return int(self._income["wage"]) + int(self._income["bonus"])


class Positon(Worker):

    def __init__(self, new_name, new_surname, new_position, new_income):
        super().__init__(new_name, new_surname, new_position, new_income)

    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return self.get_income()


engineer = Positon("Иван", "Иванов", "Инженер", {"wage": 100000, "bonus": 50000})
print(engineer.get_full_name())
print(engineer.get_total_income())
