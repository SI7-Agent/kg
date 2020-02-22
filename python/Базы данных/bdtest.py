def show_menu():
    print('Меню: ')
    print('1) Создать новую базу данных')
    print('2) Открыть существующую базу данных')
    print('3) Добавить новую запись')
    print('4) Просмотреть все записи')
    print('5) Поиск элемента')
    print('6) Отфильтровать элементы в заданном диапазоне')
    print('7) Удаление элемента по фильтру')
    print('8) Выйти', '\n')
def BD_NAME():
    directory = os.getcwd()
    files = os.listdir(directory)
    for i in range(len(files)):
        if '.db' in files[i]:
            print(files[i])
    choose = input('\nВыберите нужную БД: ')
    print()
    while choose not in files:
        print('WARNING! Файл не найден')
        choose = input('Повторите попытку: ')
    return choose
import pickle
import os
while 1:
    show_menu()
    n = input('Опция №')
    print()
    if n == '1':
        BD_NAME0 = input('Назовите БД: ') + '.db'
        with open(BD_NAME0, 'wb') as f:
            d1 = []
            d = {}
            s = 'n'
            s1 = 'n'
            while s1 == 'n':
                d1.append(input('Введите параметр: '))
                s1 = input('Закончить добавление параметров? y/n')
            while s == 'n':
                d0 = {}
                q = input('Ввод наименования предмета: ')
                for i in range(len(d1)):
                    b = d1[i]
                    print(d1[i], ' = ', end = '')
                    b1 = input()
                    d0[b] = b1
                d[q] = d0
                s = input('Закончить добавление записей? y/n ')
            d1.append(d)
            pickle.dump(d1, f)
        f.close()

    elif n == '2':
        choose = BD_NAME()

    elif n == '3':
        choose = BD_NAME()
        with open(choose, 'rb') as f:
            d = pickle.load(f)
            print(d[len(d) - 1])
        f.close()
        d1 = []
        d_temp0 = {}
        d_temp = d[len(d) - 1]
        for i in range(len(d) - 1):
            d1.append(d[i])
        with open(choose, 'ab') as f:
            s = 'n'
            while s == 'n':
                d0 = {}
                q = input('Ввод наименования предмета: ')
                for i in range(len(d1)):
                    b = d1[i]
                    print(d1[i], ' = ', end = '')
                    b1 = input()
                    d_temp0[b] = b1
                d_temp[q] = d_temp0
                s = input('Закончить добавление записей? y/n ')
            d = d1.append(d_temp)
            print(d1)
            d = d1
            print(d)
        f.close()
        with open(choose, 'wb') as f:
            pickle.dump(d, f)

    elif n == '4':
        choose = BD_NAME()
        with open(choose, 'rb') as f:
            d = pickle.load(f)
        d1 = d[len(d) - 1]
        for key, item in d1.items():
            a = key
            b = item
            print(a, ': ', sep=' ', end='')
            print(d1.get(a))
        print()

    elif n == '5':
        # choose = BD_NAME()
        # with open(choose, 'rb') as f:
        #     d = pickle.load(f)
        # search = input('Что нужно найти? ')
        # #if search in d.values():
        pass

    elif n == '6':
        # choose = BD_NAME()
        # with open(choose, 'rb') as f:
        #     d = pickle.load(f)
        # leftcorn = float(input('Ввод левого края диапазона поиска: '))
        # rightcorn = float(input('Ввод правого диапазона поиска: '))
        # d1 = d[len(d) - 1]
        # for i in range(len(d1)):
        #     if d1.get()
        pass

    elif n == '7':
        # choose = BD_NAME()
        # with open(choose, 'rb') as f:
        #     d = pickle.load(f)
        # print(d)
        # to_delete = input('Какой элемент удалить? ')
        # a = ''
        # b = ''
        # for key, item in d.items():
        #     a = key
        #     b = item
        #     if b == to_delete:
        #         d.pop(a, b)
        # print(d)
        pass

    elif n == '8':
        break

    else:
        print('Введено неверное значение!\n')