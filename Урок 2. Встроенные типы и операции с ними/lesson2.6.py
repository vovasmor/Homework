# Шаблон товара с вопросом к пользователю и ожидаемым типом данных
product_dict={
    'название': ('имя товара', str),
    'цена': ('цена товара', int),
    'количество': ('количество товара', int),
    'ед': ('единицы измерения (шт, кг и т.д.)', str),
}

# Флаг для понимания необходимости ввода еще одного товара в список или нет
next_enter = True

# Автоинкримент для номера товара
auto_inc = 1

# Список для хранения наших товаров
product_list = []


while next_enter:
    # словарь, в который мы будем заполнять атрибуты товара
    product = {}
    # заполняем товар по шаблону
    for key, value in product_dict.items():
        # цикл while True я использую для того чтобы переспросить вопрос если будет неверный ввод по типу
        while True:
            user_value = input(f'{value[0]}\n')
            try:
                user_value = value[1](user_value)
            except ValueError as e:
                print(f'{e}\nНе верное значение данных')
                continue
            product[key] = user_value
            break
    product_list.append((auto_inc, product))
    auto_inc += 1

    # тут мы проверим надо еще товар вводить или нет
    while True:
        next_add = input('Добавить еще продукт? Да/Нет\n')
        if next_add.lower() in ('да', 'нет'):
            next_enter = next_add.lower() == 'да'
            break
        else:
            print('Неверный ввод, повторите')


# Собираем словарь аналитики
product_analytics = {key: [itm[1][key] for itm in product_list] for key in product_dict}

print(product_list)
print(product_analytics)
