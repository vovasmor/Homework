number = input("Введите число n: ")
if number.isdigit():
    result = int(number) + int(number*2) + int(number*3)
    print(f"{number} + {number*2} + {number*3} = {result}")
    input()     # Задержка консоли
else:
    print("Ошибка! Необходимо ввести число.")
