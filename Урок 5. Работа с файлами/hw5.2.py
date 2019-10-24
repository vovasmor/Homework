"""

Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.

"""
with open("hw5_2.txt", "r") as my_f:
    lines = 0       # Считаем строки
    for line in my_f:
        lines += 1

        flag = 0    # Считаем только слова, а не буквы
        word = 0    # Считаем слова
        for letter in line:
            print(letter)
            if letter != ' ' and flag == 0:
                word += 1
                flag = 1
            elif letter == ' ':
                flag = 0

        print(f"{line}{word} сл.\n")
    print('Всего', lines, 'стр.')
