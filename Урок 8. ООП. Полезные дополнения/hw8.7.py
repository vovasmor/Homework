"""

Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта, создав экземпляры класса (комплексные числа)
и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.

"""


class Complex:
    def __init__(self, number):
        self.number = number

    # Cумма
    def __add__(self, other):
        return self.number + other.number

    # Умножение
    def __mul__(self, other):
        return self.number * other.number


n_1 = Complex(complex(2, 2))
n_2 = Complex(complex(5, 1))
print(n_1 * n_2)
print(n_1 + n_2)
