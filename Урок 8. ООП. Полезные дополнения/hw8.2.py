"""

Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию
и не завершиться с ошибкой.

"""


class OwnError(ZeroDivisionError):
    def __init__(self, txt):
        self.txt = txt


number_1 = input("Введите делимое: ")
number_2 = input("Введите делитель: ")

try:
    # Проверим, что обе переменные числа
    number_2 = int(number_2)
    number_1 = int(number_1)
    # Проверка, что делитель не ноль
    if number_2 == 0:
        raise OwnError("Делить на ноль нельзя!")
except ValueError:
    print("Вы ввели не число")
except OwnError as err:
    print(err)
else:
    print(f"Результат: {number_1 / number_2}")
