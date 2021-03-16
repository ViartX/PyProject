# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    speed: int
    color: str
    name: str
    is_police: bool

    def go(self):
        print("Машина поехала")

    def stop(self):
        print("Машина остановилась")

    def turn(self, direction):
        print(f"Машина повернула {direction}")

    def show_speed(self, speed):
        self.speed = speed
        print(f"Скорость машины {speed} км/ч")


class TownCar(Car):
    def __init__(self, speed, color, name, is_police = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def show_speed(self, speed):
        self.speed = speed
        if self.speed > 60:
            print(f"Внимание: скорость превышена")
        else:
            print(f"Скорость машины {self.speed} км/ч")


class SportCar(Car):
    def __init__(self, speed, color, name, is_police = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def show_speed(self, speed):
        self.speed = speed
        if self.speed > 40:
            print(f"Внимание: скорость превышена")
        else:
            print(f"Скорость машины {self.speed} км/ч")


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police = True):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police


car1 = TownCar(40, "white", "Ford")
car1.go()
car1.show_speed(61)
car1.turn("направо")
car1.show_speed(59)

print(f"цвет машины {car1.color}")
print(f"марка машины {car1.name}")