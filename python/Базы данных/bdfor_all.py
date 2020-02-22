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
    print('4) Отфильтровать элементы от a до b (включительно)')
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
    choose = input('\nВыберите нужную БД: ') + '.bin'
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
    BD_NAME0 = input('Назовите БД: ') + '.bin'
    while BD_NAME0 in files:
        print('\nБД с таким именем уже существует!\n')
        BD_NAME0 = input('Назовите БД: ') + '.bin'
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
            d1 = []
            s0 = 'n'
            while s0 == 'n' or s0 =='т':
                attribute = input('\nВвод параметра: ')
                while attribute == '':
                    print('Параметр НЕ может быть пустым!\nПовторите попытку: ')
                    attribute = input()
                d1.append(attribute)
                s0 = input('Закончить добавление параметров? y/n ')
                while s0 not in 'ynтн':
                    print('Неверные данные!\nПовторите попытку: ')
                    s0 = input()
            d0 = []
            d0.append(d1)
            print()
            while s == 'n':
                d = {}
                for i in range(len(d1)):
                    b = d1[i]
                    print(d1[i], end = ' = ')
                    b1 = input()
                    while b1 == '':
                        print('Значение параметра НЕ может быть пустым!\nПовторите попытку: ')
                        b1 = input()
                    d[b] = b1
                d0.append(d)
                s = input('Закончить добавление записей? y/n \n')
                while s not in 'ynнт':
                    print('Неверные данные!\Повторите попытку:')
                    s = input()
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
                    d1 = d[0]
                f.close()
                with open(choose, 'ab') as f:
                    s = 'n'
                    while s == 'n':
                        d0 = {}
                        for i in range(len(d1)):
                            b = d1[i]
                            print(d1[i], end=' = ')
                            b1 = input('')
                            while b1 == '':
                                print('Значение параметра НЕ может быть пустым!\nПовторите попытку: ')
                                b1 = input()
                            d0[b] = b1
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
                    d0 = d[0]
                    for i in range(1, len(d)):
                        for key, item in d[i].items():
                            print(key, ' : ', '{:<s}'.format(item), sep='',
                                  end=' ' * (30 - len(key) - len(item) - 1))
                        print()
                print()
            elif n0 == '3':
                with open(choose, 'rb') as f:
                    d = pickle.load(f)
                search = input('Что нужно найти: ')
                print()
                count = 0
                for i in range(1, len(d)):
                    for key, item in d[i].items():
                        if d[i][key] == search:
                            for key, item in d[i].items():
                                print(key, ' : ', '{:<s}'.format(item), sep='',
                                      end=' ' * (25 - len(key) - len(item) - 1))
                            print()
                        else:
                            count += 1
                count0 = 0
                for i in range(1, len(d)):
                    count0 += len(d[i].items())
                if count == count0:
                    print('\nСовпадений не найдено!')
                print()
            elif n0 == '4':
                with open(choose, 'rb') as f:
                    d = pickle.load(f)
                left_edge = input('Ввод левого края задаваемого диапазона: ')
                right_edge = input('Ввод правого края задаваемого диапазона: ')
                while left_edge > right_edge:
                    print('\nЛевый край должен быть МЕНЬШЕ правого\nПовторите попытку: ')
                    left_edge = input('\nЛевый край: ')
                    right_edge = input('\nПравый край: ')
                print()
                count = 0
                for i in range(1, len(d)):
                    for key, item in d[i].items():
                        if left_edge <= d[i].get(key) <= right_edge:
                            for key, item in d[i].items():
                                print(key, ' : ', '{:<s}'.format(item), sep='',
                                    end=' ' * (40 - len(key) - len(item) - 1))
                            print()
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
                print('Неверные данные\n')
    elif n == '3':
        break
    else:
        print('Неверные данные\n')