# 1. Реализовать класс Matrix (матрица).
# Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
# (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой
# матрицы складываем с первым элементом первой строки второй матрицы и т.д.


# Класс матрица
class Matrix:
    def __init__(self, data_input: []):
        self.data = data_input

    def __str__(self):
        result = ""

        if len(self.data) == 0:
            return "Матрица пуста"

        result += "[\n"

        for i in range(0, len(self.data)):
            i_list = self.data[i]
            result += f"   {str(i_list)}\n"

        result += "]\n"
        return result

    def __add__(self, second):
        empty = Matrix([])
        result = []

        if len(self.data) != len(second.data):
            print("Размерности матриц не совпадают")
            return empty

        for i in range(0, len(self.data)):
            if len(self.data[i]) != len(second.data[i]):
                print("Размерности матриц не совпадают")
                return empty
            new_line = []
            for j in range(0, len(self.data[i])):
                new_line.append(self.data[i][j] + second.data[i][j])
            result.append(new_line)

        return Matrix(result)


m1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
m2 = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
m3 = Matrix([[1, 2], [3, 4]])
print(str(m1))
m_summa = m1 + m2
print(str(m_summa))
