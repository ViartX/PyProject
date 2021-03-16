# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

class Clother:
    russian_name = "Одежда"

    def count_cloth(self):
        return 0


class Suit(Clother):
    russian_name = "Костюм"

    def __init__(self, exact_height):
        self.height = exact_height

    @property
    def get_height(self):
        return self.height

    @property
    def count_cloth(self):
        return 2 * self.height + 3


class Coat(Clother):
    russian_name = "Пальто"

    def __init__(self, exact_size):
        self.size = exact_size

    @property
    def get_size(self):
        return self.size

    @property
    def count_cloth(self):
        return self.size / 6.5 + 0.5


my_coat = Coat(45)
my_suit = Suit(1.80)

#print(f"{my_coat.russian_name} размера {my_coat.get_size()} требует такани {my_coat.count_cloth()} кв.м")
#print(f"{my_suit.russian_name} размера {my_suit.get_height()} требует такани {my_suit.count_cloth()} кв.м")

print(f"{my_coat.russian_name} размера {my_coat.get_size} требует такани {my_coat.count_cloth} кв.м")
print(f"{my_suit.russian_name} размера {my_suit.get_height} требует такани {my_suit.count_cloth} кв.м")