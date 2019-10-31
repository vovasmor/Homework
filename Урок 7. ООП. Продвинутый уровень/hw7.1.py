"""

Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.

Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц)
Результатом сложения должна быть новая матрица.

Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и т.д.

"""


class Matrix:
    def __init__(self, matrix):
        """
        :param matrix: list
        """
        self.matrix = matrix

    # Выводим привычный вил матрицы
    def __str__(self):
        return '\n'.join(['\t'.join(['%d' % i for i in el]) for el in self.matrix])

    # Складываем две матрицы в одну новую
    def __add__(self, other):
        result = []
        numbers = []

        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                summa = self.matrix[i][j] + other.matrix[i][j]
                numbers.append(summa)
                if len(numbers) == len(self.matrix):
                    result.append(numbers)
                    numbers = []

        return Matrix(result)


m_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
m_2 = Matrix([[5, 1, 3], [8, 4, 7], [1, 9, 14]])
print(f"Первая матрица: \n{m_1},\nВторая матрица: \n{m_2}",)
print(f"Результат сложения матриц: \n{m_1 + m_2}")
