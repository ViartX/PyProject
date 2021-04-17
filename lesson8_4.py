# 4. Начните работу над проектом «Склад оргтехники».
# Создайте класс, описывающий склад. А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад
# и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
# можно использовать любую подходящую структуру, например словарь.

# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
# изученных на уроках по ООП.


class Store:

    store_base = {}         # device:quantity

    def __init__(self, str_address):
        self.address = str_address

    def to_store(self, device, quantity):
        current = self.store_base.get(device)
        if current is None:          # добавляем новую запись в книге
            self.store_base[device] = quantity
            print(f"Товар {device} доставлен на склад, было 0 стало {quantity}")
        else:                       # добаляем единицы для данной позиции
            self.store_base[device] = current + quantity
            print(f"Товар {device} добавлен на склад, было {current} стало {current + quantity}")

    def from_store(self, device, quantity):
        current = self.store_base.get(device)
        if current is None:
            print(f"Товар {device} отсутствует на складе")
        elif current < quantity:
            print(f"Товара {device} недостаточно для выдачи")
        else:
            self.store_base[device] = current - quantity
            print(f"Товар {device} выдан в размере {quantity} ед.")
            if self.store_base[device] == 0:
                self.store_base.pop(device)
                print(f"Товар {device} закончился")

class Device:
    brand: str
    model: str
    art: str

    def __init__(self, str_brand, str_model, str_art):
        self.brand = str_brand
        self.model = str_model
        self.art = str_art


class Printer(Device):
    type: str
    dpi: str
    paper_size: str
    color: bool

    def __init__(self, str_brand, str_model, str_art, str_type, str_dpi, str_paper_size, str_color="True"):
        self.brand = str_brand
        self.model = str_model
        self.art = str_art
        self.type = str_type
        self.dpi = str_dpi
        self.paper_size = str_paper_size
        self.color = bool(str_color)


class Scanner(Device):
    type: str
    dpi: str
    paper_size: str

    def __init__(self, str_brand, str_model, str_art, str_type, str_dpi, str_paper_size):
        self.brand = str_brand
        self.model = str_model
        self.art = str_art
        self.type = str_type
        self.dpi = str_dpi
        self.paper_size = str_paper_size


class Xerox(Device):
    type: str
    paper_size: str

    def __init__(self, str_brand, str_model, str_art, str_type, str_paper_size):
        self.brand = str_brand
        self.model = str_model
        self.art = str_art
        self.type = str_type
        self.paper_size = str_paper_size


class NotValidNum(Exception):
    def __init__(self, txt):
        self.txt = txt


xerox1 = Xerox("HP", "5501", "x1", "laser", "A4")
printer1 = Printer("Dell", "D401", "p1", "laser", "1080","A4")

store = Store("Москва")


store.to_store(xerox1.art, 3)
print(store.store_base)

store.to_store(xerox1.art, 2)
print(store.store_base)

store.from_store(xerox1.art, 6)
print(store.store_base)

store.from_store(printer1.art, 5)
print(store.store_base)


while True:
    input_str = input('выберете действие: "+" - внести товар, "-" - изъять товар, "q" - выйти: ')
    if input_str == "q":
        break
    if input_str == "+":        # внесение на склад
        device_str = input('ведите тип товара: принтер, ксерокс, сканер: ')
        if device_str not in ["принтер", "ксерокс", "сканер"]:
            print("Указан недопустимый вид товара")
            continue
        art_str = input('ведите артикул: ')
        quantity_str = input('ведите количество: ')
        new_device = Device("not defined", "not defined", art_str)

        try:
            if not quantity_str.isdigit():
                raise NotValidNum("Ошибка при вводе числа")
            quantity_int = int(quantity_str)
            store.to_store(new_device.art, quantity_int)
            print(store.store_base)
        except NotValidNum as err:
            print(err)
            break

    if input_str == "-":  # расход со склада
        device_str = input('ведите тип товара: принтер, ксерокс, сканер: ')
        if device_str not in ["принтер", "ксерокс", "сканер"]:
            print("Указан недопустимый вид товара")
            continue
        art_str = input('ведите артикул: ')
        quantity_str = input('ведите количество: ')

        try:
            if not quantity_str.isdigit():
                raise NotValidNum("Ошибка при вводе числа")
            quantity_int = int(quantity_str)
            store.from_store(art_str, quantity_int)
            print(store.store_base)
        except NotValidNum as err:
            print(err)
            break


print(store.store_base)

