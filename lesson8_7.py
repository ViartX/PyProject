# 7. Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение
# созданных экземпляров. Проверьте корректность полученного результата.

class Complex:
    real: float
    img: float

    def __init__(self, real, img):
        self.real = real
        self.img = img

    def __str__(self):
        return (f"{self.real} + {self.img}i")

    def __add__(self, other):
        return Complex(self.real + other.real, self.img + other.img)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.img - other.img)

    def __mul__(self, other):
        real = self.real * other.real - self.img * other.img
        img = self.img * other.real + self.real * other.img
        return Complex(real, img)


c1 = Complex(2.0, 3.0)
print(c1)
c2 = Complex(1.0, 2.0)
print(c2)
c3 = c1 + c2
print(c3)
c4 = c3 - c2
print(c4)
c5 = c1 * c2
print(c5)