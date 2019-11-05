"""

Создайте собственный класс-исключение,
который должен проверять содержимое списка на отсутствие элементов типа строка и булево.
Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
Класс-исключение должен контролировать типы данных элементов списка.

"""


class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


result = []
next_enter = True

while next_enter:
    my_list = [el for el in input("Введите элементы списка': ").split()]
    print(my_list)
    for item in my_list:
        try:
            if not item.isnumeric():
                raise OwnError(f"{item}-{type(item)} Такого типа не должно быть в списке!")
        except OwnError as er:
            print(er)
            continue
        result.append(item)
        print(result)

    while True:
        next_add = input('Добавить еще элемент? Да/Нет\n')
        if next_add.lower() in ('да', 'нет'):
            next_enter = next_add.lower() == 'да'
            break
        else:
            print('Неверный ввод, повторите')

print(result)


