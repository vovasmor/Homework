"""

Опишите несколько классов: TownCar, SportCar, WorkCar, PoliceCar.
У каждого класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также несколько методов: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда).

Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.

"""


class Car:
    # Определям атрибуты
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    # Методы, отвечающие за движение машины
    def go(self):
        return print("Машина поехала")

    def stop(self):
        return print("Машина остановилась")

    def turn_left(self):
        return print("Машина повернула налево")

    def turn_right(self):
        return print("Машина повернула направо")

    # Метод отвечает за скорость
    def show_speed(self):
        return self.speed


class TownCar(Car):
    # Переопределяем метод скорости
    def show_speed(self):
        if self.speed > 60:
            return "Превышении скорости"
        return self.speed


class SportCar(Car):
    pass


class WorkCar(Car):
    # Переопределяем метод скорости
    def show_speed(self):
        if self.speed > 40:
            return "Превышении скорости"
        return self.speed


class PoliceCar(Car):
    pass


town = TownCar(60, "Синий", "Mazda", False)
town.go()
print(town.show_speed(), '\n')

sport = SportCar(50, "Красный", "BMW", False)
sport.stop()
print(sport.show_speed(), '\n')

work = WorkCar(70, "Голубой", "Ford", False)
work.turn_left()
print(work.show_speed(), '\n')

police = PoliceCar(40, "Розовый", "Nissan", True)
police.turn_right()
print(police.show_speed(), '\n')

print(town.color, sport.color, work.color, police.color, '', sep='\n')
print(town.name, sport.name, work.name, police.name, sep='\n')
