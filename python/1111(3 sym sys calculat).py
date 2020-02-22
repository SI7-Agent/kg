from tkinter import *
from tkinter import messagebox

root = Tk() #Инициализация окна
root.title('Калькулятор') #Изменение заголовка
root.iconbitmap(r'C:\Users\kiril\OneDrive\Pictures\calculator.ico')
#Изменение лого
root.geometry('500x100') #Установка размеров окна

drop_menu = Menu(root) #Конфигурация пунктов меню
root.config(menu = drop_menu) #Привязка меню к родительскому окну

first_drop = Menu(drop_menu) #Подменю №1
drop_menu.add_cascade(label = 'Чистка окон', menu = first_drop)
#Изменение названия пункта меню и создание подменю

first_drop.add_command(label = 'Очистить все окна', command =
lambda: deletion_all(text_first_num, text_second_num, text_result))
#Пункт меню для очистки всех полей

new_menu = Menu(first_drop) #Конфигурация меню в подменю
first_drop.add_cascade(label = 'Очистить по одному', menu = new_menu)
#Изменение названия пункта подменю и создание подменю в подменю

new_menu.add_command(label = 'Очистить поле первого слагаемого',
                     command = lambda: text_first_num.delete(0, 'end'))
#Пункт подменю для очистки первого поля

new_menu.add_command(label = 'Очистить поле второго слагаемого',
                     command = lambda: text_second_num.delete(0, 'end'))
#Пункт подменю для очистки второго поля

new_menu.add_command(label = 'Очистить поле суммы',
                     command = lambda: deletion_sum(text_result))
#Пункт подменю для очистки последнего поля

second_drop = Menu(drop_menu) #Подменю №2
drop_menu.add_cascade(label = 'Выполнение операций', menu = second_drop)
#Изменение названия пункта меню и создание подменю
second_drop.add_command(label = 'Сложить', command =
lambda: mathmatic_plus(text_first_num, text_second_num, text_result))
#Пункт меню для сложения

second_drop.add_command(label = 'Вычесть', command=lambda:
mathmatic_minus(text_first_num, text_second_num, text_result))
#Пункт меню для вычитания

third_drop = Menu(drop_menu) #Подменю №3
drop_menu.add_cascade(label = 'Инфо', menu = third_drop)
#Изменение названия пункта меню и создание подменю

third_drop.add_command(label = 'О программе', command = lambda: info())
#Пункт меню для отображения информации о программе и разработчике

btn_plus = Button(text = 'Сложить', width = 10, command = lambda:
mathmatic_plus(text_first_num, text_second_num, text_result))
#Создание кнопки 'сложить'

btn_plus.place(x = 280, y = 40) #Расположение кнопки 'сложить'

btn_minus = Button(text = 'Вычесть', width = 10, command = lambda:
mathmatic_minus(text_first_num, text_second_num, text_result))
#Создание кнопки 'вычесть'

btn_minus.place(x = 280, y = 70) #Расположение кнопки 'вычесть'

def win1(f):
    flag.set(1)

def win2(f):
    flag.set(2)

text_first_var = StringVar()
text_first_num = Entry(textvariable = text_first_var, width = 15)
#Создание поля ввода первого слагаемого
text_first_num.place(x = 10, y = 15)
text_first_num.bind('<Button-1>', win1)
#Расположение поля ввода первого слагаемого

text_second_var = StringVar()
text_second_num = Entry(textvariable = text_second_var, width = 15)
#Создание поля ввода второго слагаемого
text_second_num.place(x = 190, y = 15)
text_second_num.bind('<Button-1>', win2)
#Расположение поля ввода второго слагаемого

lbl_equal = Label(text = '=') #Создание знака 'равно'
lbl_equal.place(x = 315, y = 15) #Расположение знака 'равно'

plus_minus = Label(text = '+/-')
plus_minus.place(x = 135, y = 15)

text_result = Label(width = 15, height = 1, bg = 'white')
#Создание вывода суммы
text_result.place(x = 370, y = 15) #Расположение вывода суммы

plus_btn = Button(text = '+', width = 4
                        , command = lambda: enter('+'))
plus_btn.place(x = 103, y = 40)

minus_btn = Button(text = '-', width = 4
                         , command = lambda: enter('-'))
minus_btn.place(x = 143, y = 40)

zero_btn = Button(text = '0', width = 10
                        , command = lambda: enter('0'))
zero_btn.place(x = 103, y = 70)

root.resizable(width = False, height = False)
#Запрет на изменение размеров окна

flag = IntVar()
s1 = Entry(textvariable = flag)

def enter(btn):
    if flag.get() == 1:
        text_first_var.set(text_first_var.get() + btn)
    elif flag.get() == 2:
        text_second_var.set(text_second_var.get() + btn)
#Функция для заполнения полей через экранные кнопки

def deletion_all(entry1, entry2, text1): #Функция очистки всех полей разом
    entry1.delete(0, 'end')
    entry2.delete(0, 'end')
    deletion_sum(text1)
    text1.destroy()
    text1 = Label(width = 15, height = 1, bg = 'white')
    text1.place(x = 370, y = 15)

def deletion_sum(text1): #Функция очистки поля вывода суммы
    text1.destroy()
    text1 = Label(width = 15, height = 1, bg = 'white')
    text1.place(x = 370, y = 15)

#Функция для проверки вводимого числа на принадлежность к указанной системе
def check_input(num1):
    count = 0
    num1 = str(num1)
    if num1 == '':
        return 0
    else:
        for i in num1:
            if i in ['+', '-', '0']:
                count += 1
        if count == len(num1):
            return 1
        else:
            return 0

def mathmatic_plus(entry1, entry2, text): #Функция для реализации сложения
    num1 = entry1.get()
    num2 = entry2.get()

    if check_input(num1) == 0 or check_input(num2) == 0:
        messagebox.showerror('Error 502', 'Проверьте правильность введённых данных!')
    else:
        subresult = []

        if len(num1) > len(num2):
            num2 = '0'*(len(num1) - len(num2) + 1) + num2
            num1 = '0' + num1
        else:
            num1 = '0'*(len(num2) - len(num1) + 1) + num1
            num2 = '0' + num2

        for i in range(len(num1)-1, -1, -1):
            subresult.append(num1[i] + num2[i])

        while ('0+' in subresult or '+0' in subresult or '0-' in subresult
               or '-0' in subresult or '+-' in subresult or '-+' in subresult
               or '++' in subresult or '--' in subresult or '00' in subresult):
            result = []
            subvar = ''
            for g in subresult:
                if g == '0+' or g == '+0':
                    result.append('+' + subvar)
                    subvar = ''
                elif g == '0-' or g == '-0':
                    result.append('-' + subvar)
                    subvar = ''
                elif g == '+-' or g == '-+':
                    result.append('0' + subvar)
                    subvar = ''
                elif g == '++':
                    result.append('-' + subvar)
                    subvar = '+'
                elif g == '--':
                    result.append('+' + subvar)
                    subvar = '-'
                elif g == '00':
                    result.append('0' + subvar)
                    subvar = '0'
                else:
                    result.append(g + subvar)
            subresult = result

        result.reverse()
        if result.count('0') == len(result):
            result = []
            result.append('0')
        else:
            while result[0] == '0':
                result.pop(int(result[0]))
        text_result = ''.join(result)
        text.destroy()
        text = Label(width = 15, height = 1, bg = 'white', text = text_result)
        text.place(x = 370, y = 15)

def mathmatic_minus(entry1, entry2, text): #Функция для реализации вычитания
    num1 = entry1.get()
    num2 = entry2.get()

    if check_input(num1) == 0 or check_input(num2) == 0:
        messagebox.showerror('Error 502', 'Проверьте правильность введённых данных!')
    else:
        subresult = []

        if len(num1) >= len(num2):
            num2 = '0' * (len(num1) - len(num2) +1) + num2
            num1 = '0' + num1
        else:
            num1 = '0' * (len(num2) - len(num1)+1) + num1
            num2 = '0' + num2

        for i in range(len(num1) - 1, -1, -1):
            subresult.append(num1[i] + num2[i])

        while ('0+' in subresult or '+0' in subresult or '0-' in subresult
               or '-0' in subresult or '+-' in subresult or '-+' in subresult
               or '++' in subresult or '--' in subresult or '00' in subresult):
            result = []
            subvar = ''
            for g in subresult:
                if g == '0+':
                    result.append('-' + subvar)
                    subvar = ''
                elif g == '+0':
                    result.append('+' + subvar)
                    subvar = ''
                elif g == '0-':
                    result.append('+' + subvar)
                    subvar = ''
                elif g == '-0':
                    result.append('-' + subvar)
                    subvar = ''
                elif g == '+-':
                    result.append('-' + subvar)
                    subvar = '-'
                elif g == '-+':
                    result.append('+' + subvar)
                    subvar = '+'
                elif g == '++':
                    result.append('0' + subvar)
                    subvar = ''
                elif g == '--':
                    result.append('0' + subvar)
                    subvar = ''
                elif g == '00':
                    result.append('0' + subvar)
                    subvar = ''
                else:
                    result.append(g + subvar)
            subresult = result

        result.reverse()
        if result.count('0') == len(result):
            result = []
            result.append('0')
        else:
            while result[0] == '0':
                result.pop(int(result[0]))
        text_result = ''.join(result)
        text.destroy()
        text = Label(width = 15, height = 1, bg = 'white', text = text_result)
        text.place(x = 370, y = 15)

def info(): #Функция для вывода информации о программе и разработчике
    messagebox.showinfo('Информация', '\u00A9 Собственность разработчика\n\n'
                                      'Программа для выполнения арифметических действий в троичной симметричной '
                                      'системе. \n\n'
                                      'Разработано Рудневым Кириллом, ИУ7-25, 2018г.')

root.mainloop()
