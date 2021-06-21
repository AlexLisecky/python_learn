# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.

class Matrix:
    def __init__(self, matrix_1, matrix_2):
        self.matrix_1 = matrix_1
        self.matrix_2 = matrix_2

    def __str__(self, ):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in result]))

    def __add__(self):
        result = [[0, 0],
                  [0, 0],
                  [0, 0]]
        for i in range(len(self.matrix_1)):
            for j in range(len(self.matrix_1[0])):
                result[i][j] = self.matrix_1[i][j] + self.matrix_2[i][j]
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in result]))


matrix = Matrix([[1, 2],
                 [3, 4],
                 [5, 6]],
                [[1, 2],
                 [3, 4],
                 [5, 6]])
print(matrix.__add__())
