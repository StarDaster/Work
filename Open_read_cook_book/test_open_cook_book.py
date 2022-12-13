from pprint import pprint
import operator
import os

'''
Омлет
3
Яйцо | 2 | шт.
Молоко | 100 | мл.
Помидор | 2 | шт.

Утка по-пекински
4
Утка | 1 | шт.
Вода | 2 | л.
Мед | 3 | ст.л.
Соевый соус | 60 | мл.

Запеченный картофель
3
Картофель | 1 | кг.
Чеснок | 3 | зуб.
Сыр гауда | 100 | г.

Фахитос
5
Говядина | 500 | г.
Перец сладкий | 1 | шт.
Лаваш | 2 | шт.
Винный уксус | 1 | ст.л.
Помидор | 2 | шт.

Драники
5
Картофель | 1 | кг.
Соль | 1 | чай.л.
Яйцо | 1 | ст.л.
Перец | 1 | чай.л.
Чеснок | 1 | шт.
'''


def read_cook_book():
    file_path = os.path.join(os.getcwd(), 'recipes.txt')
    cook_book = {}
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            dish_name = line.strip()
            count = int(f.readline())
            ing_list = list()
            for item in range(count):
                ingrs = {}
                ingr = f.readline().strip()
                ingrs['ingredient_name'], ingrs['quantity'], ingrs['measure'] = ingr.split('|')
                ingrs['quantity'] = int(ingrs['quantity'])
                ing_list.append(ingrs)
            f.readline()
            cook_book[dish_name] = ing_list
    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    ingr_list = dict()

    for dish_name in dishes:  # итерируем список полученных блюд
        if dish_name in cook_book:
            for ings in cook_book[dish_name]:  # итерируем ингридиенты в блюде
                meas_quan_list = dict()
                if ings['ingredient_name'] not in ingr_list:
                    meas_quan_list['measure'] = ings['measure']
                    meas_quan_list['quantity'] = ings['quantity'] * person_count
                    ingr_list[ings['ingredient_name']] = meas_quan_list
                else:
                    ingr_list[ings['ingredient_name']]['quantity'] = ingr_list[ings['ingredient_name']]['quantity'] + \
                                                                     ings['quantity'] * person_count

        else:
            print(f'\n"Такого блюда нет в списке!"\n')
    return ingr_list


if __name__ == '__main__':
    filename = "recipes.txt"
    cook_book = read_cook_book()
    print('Задание 1------------------------------------------------------------>')
    print(cook_book)
    print('Задание 2------------------------------------------------------------>')
    pprint(get_shop_list_by_dishes(dishes=['Омлет', 'Утка по-пекински', 'Запеченный картофель', 'Фахитос', 'Драники'],
                                   person_count=1))
