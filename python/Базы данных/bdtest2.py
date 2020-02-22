def show_main_menu():
    print('Меню: ')
    print('1) Создать новую базу данных')
    print('2) Открыть существующую базу данных')
    print('3) Выйти', '\n')

def show_dop_menu():
    print('Подменю: ')
    print('1) Добавить новую запись')
    print('2) Просмотреть все записи')
    print('3) Поиск элемента')
    print('4) Отфильтровать элементы по стоимости от a до b (включительно)')
    print('5) Удаление элемента по фильтру')
    print('6) Вернуться', '\n')

def BD_NAME():
    directory = os.getcwd()
    files = os.listdir(directory)
    filetemp = []
    for i in range(len(files)):
        if '.bin' in files[i]:
            filetemp.append(files[i])
            print(files[i])
    choose = input('\nВыберите нужную БД: ')
    while choose not in files:
        print('\nWARNING! Файл не найден')
        choose = input('Повторите попытку: ')
    if len(filetemp) == 0:
        print('БД не обнаружено!')
        return quit()
    return choose

def check():
    directory = os.getcwd()
    files = os.listdir(directory)
    BD_NAME0 = input('Назовите БД: ')
    while ('/' in BD_NAME0 or
                        '\u005c' in BD_NAME0 or
                        '?' in BD_NAME0 or
                        ':' in BD_NAME0 or
                        '*' in BD_NAME0 or
                        '<' in BD_NAME0 or
                        '>' in BD_NAME0 or
                        '|' in BD_NAME0) or BD_NAME0 in files:
            print('Имя содержит недопустимые символы или БД уже существует\nПовторите попытку')
            BD_NAME0 = input('Назовите БД: ')

    return BD_NAME0

import pickle
import os
while 1:
    show_main_menu()
    n = input()
    print()
    if n == '1':
        BD_NAME0 = check()
        with open(BD_NAME0, 'wb') as f:
            s = 'n'
            d1 = ['Наименование', 'Стоимость', 'ОС', 'Год выпуска', 'Рейтинг']
            d0 = []
            d0.append(d1)
            pickle.dump(d0, f)
        f.close()
        print()
    elif n == '2':
        choose = BD_NAME()
        print()
        while 1:
            show_dop_menu()
            n0 = input()
            print()
            if n0 == '1':
                with open(choose, 'rb') as f:
                    d = pickle.load(f)
                    f.close()
                    d1 = d[0]
                    d0 = {}
                    with open(choose, 'ab') as f:
                        s = 'n'
                        while s == 'n':
                            d0 = {}
                            name = input('Ввод наименования: ')
                            price = input('Ввод стоимости: ')
                            while price.isdigit() == 0:
                                print('\nНеверные данные!\nВведите целое положительное значение стоимости: ')
                                price = input()
                                print()
                            sys = input('Ввод ОС: ')
                            year = input('Ввод года выпуска: ')
                            while year.isdigit() == 0 or (int(year) < 1800 or int(year) > 2017):
                                print('\nНеверные данные!\nВведите значение года выпуска от 1800 до 2017')
                                year = input()
                                print()
                            rate = input('Ввод рейтинга: ')
                            while rate.isdigit() == 0 or (int(rate) < 0 or int(rate) > 100):
                                print('\nНеверные данные!\nВведите значение рейтинга в виде целого числа от 0 до 100')
                                rate = input()
                                print()
                            d0[d1[0]] = name
                            d0[d1[1]] = price
                            d0[d1[2]] = sys
                            d0[d1[3]] = year
                            d0[d1[4]] = rate
                            d.append(d0)
                            s = input('Закончить добавление записей? y/n ')
                            while s not in 'ynнт':
                                print('Неверные данные!\Повторите попытку:')
                                s = input()
                    f.close()
                    with open(choose, 'wb') as f:
                        pickle.dump(d, f)
                print()
            elif n0 == '2':
                with open(choose, 'rb') as f:
                    d = pickle.load(f)
                    d0 = {}
                    d1 = d[0]
                    for i in range(len(d1)):
                        print(d1[i], end = ' '*10)
                    print()
                    for i in range(1, len(d)):
                        d0 = dict(d[i])
                        for j in d0.keys():
                            if len(j) > len(d0.get(j)):
                                print(d0.get(j), end = ' ' * (abs((len(j) - len(d0.get(j)))) + 10))
                            else:
                                print(d0.get(j), end=' ' * (12 - len(d0.get(j))))
                        print()
                print()
            elif n0 == '3':
                with open(choose, 'rb') as f:
                    d = pickle.load(f)
                search = input('Что нужно найти: ')
                while search == '' or len(search) == search.count(' '):
                    print('\nПоле не может быть пустым\nПовторите попытку:')
                    search = input()
                print()
                count = 0
                d0 = {}
                d1 = d[0]
                for i in range(len(d1)):
                    print(d1[i], end=' ' * 10)
                print()
                for i in range(1, len(d)):
                    co = 0
                    for key, item in d[i].items():
                        # if d[i][key] == search:
                        if co < 1:
                            if search in d[i].get(key):
                                co += 1
                                d0 = dict(d[i])
                                for j in d0.keys():
                                    if len(j) > len(d0.get(j)):
                                        print(d0.get(j), end=' ' * (abs((len(j) - len(d0.get(j)))) + 10))
                                    else:
                                        print(d0.get(j), end=' ' * (12 - len(d0.get(j))))
                                print()
                            else:
                                count += 1
                count0 = 0
                for i in range(1, len(d)):
                    count0 += len(d[i].items())
                if count == count0:
                    print('\nСовпадений не найдено!')
                print('\n')
            elif n0 == '4':
                with open(choose, 'rb') as f:
                    d = pickle.load(f)
                left_edge = input('Ввод левого края задаваемого диапазона: ')
                right_edge = input('Ввод правого края задаваемого диапазона: ')
                while left_edge.isdigit() == 0 or right_edge.isdigit() == 0:
                    print('\nВведите верные числа:')
                    left_edge = input('\nЛевый край: ')
                    right_edge = input('Правый край: ')
                    while left_edge > right_edge:
                        print('\nЛевый край должен быть МЕНЬШЕ правого\nПовторите попытку: ')
                        left_edge = input('\nЛевый край: ')
                        right_edge = input('Правый край: ')
                print()
                count = 0
                d0 = {}
                d1 = d[0]
                for i in range(len(d1)):
                    print(d1[i], end=' ' * 10)
                if left_edge == right_edge:
                    print()
                print()
                for i in range(1, len(d)):
                    for key, item in d[i].items():
                        if left_edge <= d[i].get(d[0][1]) <= right_edge:
                            d0 = dict(d[i])
                            for j in d0.keys():
                                if len(j) > len(d0.get(j)):
                                    print(d0.get(j), end=' ' * (abs((len(j) - len(d0.get(j)))) + 10))
                                else:
                                    print(d0.get(j), end=' ' * (12 - len(d0.get(j))))
                            print()
                            break
                        else:
                            count += 1
                count0 = 0
                for i in range(1, len(d)):
                    count0 += len(d[i].items())
                if count == count0:
                    print('\nСовпадений не найдено!')
                print()
            elif n0 == '5':
                with open(choose, 'rb') as f:
                    d = pickle.load(f)
                delete = input('Ввод фильтра для удаления: ')
                while delete == '':
                    print('\nФильтр НЕ может быть пустым!\nПовторите попытку:\n')
                    delete = input('Ввод фильтра: ')
                count = 0
                deltemp = []
                for i in range(1, len(d)):
                    for key, item in d[i].items():
                        if d[i][key] == delete:
                            deltemp.append(d[i])
                        else:
                            count += 1
                count0 = 0
                for i in range(1, len(d)):
                    count0 += len(d[i].items())
                if count == count0:
                    print('\nЭлементов для удаления не найдено!')
                print()
                for g in deltemp:
                    while g in d:
                        d.remove(g)
                f.close()
                with open(choose, 'wb') as f:
                    pickle.dump(d, f)
            elif n0 == '6':
                break
            else:
                print('Выбрана несуществующая функция\n')
    elif n == '3':
        break
    else:
        print('Выбрана несуществующая функция\n')