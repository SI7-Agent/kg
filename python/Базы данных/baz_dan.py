# def get_dict():
#     d1 = dict(d.values)
#     return d1

def BD_NAME():
    directory = os.getcwd()
    files = os.listdir(directory)
    for i in range(len(files)):
        if '.db' in files[i]:
            print(files[i])
    choose = input('\nВыберите нужную БД: ')
    while choose not in files:
        print('WARNING! Файл не найден')
        choose = input('Повторите попытку: ')
    return choose
import pickle
import os
while 1:
    print('Меню: ')
    print('1) Создать новую базу данных')
    print('2) Открыть существующую базу данных')
    print('3) Добавить новую запись')
    print('4) Просмотреть все записи')
    print('5) Поиск элемента')
    print('6) Отфильтровать элементы в заданном диапазоне')
    print('7) Удаление элемента по фильтру')
    print('8) Выйти', '\n')
    n = input('Опция №')
    print()
    if n == '1':
        BD_NAME0 = input('Назовите БД: ') + '.db'
        with open(BD_NAME0, 'wb') as f:
            d = {}
            s = 'n'
            i = 1
            while s == 'n':
                b = input('Ввод параметра: ')
                b1 = input('Ввод значения параметра: ')
                s = input('Закончить добавление параметров? y/n ')
                d[b] = b1
            i += 1
            pickle.dump(d, f)
        print(d)
    elif n == '2':
        choose = BD_NAME()
        with open(choose, 'rb') as f:
            d = pickle.load(f)
            print(d)
            print(d.values())
    elif n == '3':
        choose = BD_NAME()
        with open(choose, 'rb') as f:
            d = pickle.load(f)
            print(d)
        f.close()
        with open(choose, 'ab') as f:
            s0 = 'n'
            i = len(d)
            while s0 == 'n':
                a2 = input('Ввод нового параметра: ')
                a3 = input('Ввод значения нового параметра: \n')
                d[a2] = a3
                i += 1
                s0 = input('Закончить добавление записей? y/n \n')
        print(d)
    elif n == '4':
        choose = BD_NAME()
        with open(choose, 'rb') as f:
            d = pickle.load(f)
            print(d)
            print()
    elif n == '5':
        choose = BD_NAME()
        with open(choose, 'rb') as f:
            d = pickle.load(f)
        search = input('Что нужно найти? ')
        #if search in d.values():

    elif n == '6':
        choose = BD_NAME()
        with open(choose, 'rb') as f:
            d = pickle.load(f)
        leftcorn = input('')
        rightcorn = input('')

    elif n == '7':
        choose = BD_NAME()
        with open(choose, 'rb') as f:
            d = pickle.load(f)
        print(d)
        to_delete = input('Какой элемент удалить? ')
        a = ''
        b = ''
        for key, item in d.items():
            a = key
            b = item
            if b == to_delete:
                d.pop(a, b)

        print(d)
    elif n == '8':
        break
    else:
        print('Введено неверное значение!\n')