"""

Начните работу над проектом «Склад оргтехники».
Создайте класс, описывающий склад. А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.


Продолжить работу над первым заданием.
Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники,
а также других данных, можно использовать любую подходящую структуру, например словарь


Продолжить работу над вторым заданием.
Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

Подсказка:
постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.

"""


# Класс-исключение
class LessThenError(Exception):
    def __init__(self, txt):
        self.txt = txt


class Storage:
    def __init__(self, name):
        self.name = name
        self.box = {}

    def to_storage(self, item, count):
        """
        Метод отвечает за приём оргтехники на склад
        """
        if isinstance(count, int):

            if count >= 0:
                # Количество оргтехники на складе
                try:
                    self.box[str(item)] += count
                    return self.box
                except KeyError as er:
                    self.box[str(item)] = count
                    return self.box
            else:
                raise LessThenError("Количество оргтехники не может быть меньше нуля!")

        else:
            raise TypeError

    def to_workplace(self, item, count):
        """
        Метод отвечает за передачу оргтехники со склада
        """
        # Если ввести число превышающее кол-во техники на складе, то выводит предупреждение и все кол-во техники
        try:
            if self.box[str(item)] < count:
                print("На складе нет столько оргтехники!\nВыгружено максимальное количество.")
                del self.box[str(item)]
                return self.box

            else:
                self.box[str(item)] -= count
                if self.box[str(item)] == 0:
                    del self.box[str(item)]
                return self.box
        except KeyError:
            return f"Я не смог найти {item} на складе"


    @property
    def get_box(self):
        return self.box


class OffEquipment:
    def __init__(self, mass, color, name):
        self.mass = mass
        self.color = color
        self.name = name

    def __str__(self):
        return self.name


class Printer(OffEquipment):
    def __init__(self, mass, color, name, unique1):
        super().__init__(mass, color, name)
        # уникальный параметр
        self.unique1 = unique1


class Scanner(OffEquipment):
    def __init__(self, mass, color, name, unique2):
        super().__init__(mass, color, name)
        # уникальный параметр
        self.unique2 = unique2


class Copier(OffEquipment):
    def __init__(self, mass, color, name, unique3):
        super().__init__(mass, color, name)
        # уникальный параметр
        self.unique3 = unique3


store = Storage("Склад")
pri = Printer(12, "Синий", "Принтер", "Уникальный парамент1")
cop = Copier(8, "Белый", "Ксерокс", "Уникальный парамент2")
scan = Scanner(3, "Черный", "Сканер", "Уникальный парамент3")

print(pri, cop, scan, "", sep="\n")

print(store.to_workplace(pri, 1), "\n")

print(store.to_storage(pri, 2))
print(store.to_storage(pri, 3), "\n")

print(store.to_workplace(pri, 3))
print(store.to_workplace(pri, 1000000))
