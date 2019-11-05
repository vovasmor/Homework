"""

Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода.
Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.

"""


class Date:

    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def to_int(cls, date):
        day, month, year = map(int, date.split('-'))
        return f"{day:02} {month:02} {year}"

    @staticmethod
    def valid(date):
        day, month, year = map(int, date.split('-'))
        return day <= 31 and month <= 12 and year <= 9999


print(Date.to_int('12-12-2012'))
print(Date.valid('12-12-2012'))


