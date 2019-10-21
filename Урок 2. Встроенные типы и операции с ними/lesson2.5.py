"""
Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться после них.

"""
my_list = [14, 12, 6, 6, 2]

right = -len(my_list) + 1
i = 0

number = input("Введите число: ")
if number.isdigit():
    number = int(number)

    while i < len(my_list):
        if right != 0:      # Если right = 0, то number наименьшее число в списке. Добавляем его в конец.
            if number > my_list[i]:
                my_list.insert(i, number)
                print(my_list)
                break

            else:
                right += 1
                i += 1

        else:
            my_list.append(number)
            print(my_list)
            right += 1
            i += 1

else:
    print("Ошибка! Необходимо ввести число.")