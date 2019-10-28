"""

Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname,
position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
оклад и премия, например, {"profit": profit, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
и дохода с учетом премии (get_full_profit).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров).

"""


class Worker:
    # Определям атрибуты
    def __init__(self, name, surname, position, _income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = _income


class Position(Worker):
    # Метод получения полного имени сотрудника
    def get_full_name(self):
        return print(self.surname + ' ' + self.name)

    # Метод дохода с учетом премии
    def get_full_profit(self):
        return print(int(self._income["profit"]) + int(self._income["bonus"]))


a_1= Position('Олег', 'Где макет', 'дизайнер-макетчик', {"profit": 58000, "bonus": 12000})
a_1.get_full_name()
a_1.get_full_profit()
a_2 = Position('Сергей', 'Соломин', 'программист', {"profit": 60000, "bonus": 11500})
a_2.get_full_name()
a_2.get_full_profit()
