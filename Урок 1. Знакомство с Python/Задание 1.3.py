number = input("Введите число: ")
if number.isdigit():
    number = int(number)
    max = number % 10      # Предположим, что последняя цифра числа является наибольшей
    number //= 10        # Уничтожаем последнюю цифру числа
    while number > 0:
        if number % 10 > max:
            max = number % 10        # Если последняя цифра числа больше предыдущей, то записыпаем ее в max
        number //= 10
    print(f" Самая большая цифра: {max}")
    input()     # Задержка консоли
else:
    print("Ошибка! Необходимо ввести число.")
