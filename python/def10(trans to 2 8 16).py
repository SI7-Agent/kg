from tkinter import *

root = Tk()
root.title('DEF10')
root.resizable(width = 'false', height = 'false')
root.geometry('500x100')

first = StringVar()
first_text = Entry(textvariable = first, width = 15)
first_text.place(x = 10, y = 10)

first_btn = Button(width = 10, text = 'Нажать', command = lambda: first_filled(first_text))
first_btn.place(x = 10, y = 35)

second = StringVar()
second_text = Entry(textvariable = second, width = 15)
second_text.place(x = 150, y = 10)

second_btn = Button(width = 10, text = 'Нажать', command = lambda: second_filled(second_text))
second_btn.place(x = 150, y = 35)

third = StringVar()
third_text = Entry(textvariable = third, width = 15)
third_text.place(x = 300, y = 10)

third_btn = Button(width = 10, text = 'Нажать', command = lambda: third_filled(third_text))
third_btn.place(x = 300, y = 35)

def first_filled(text1):
    num = str(text1.get())

    if len(num) % 3 != 0:
        num1 = (3 - len(num) % 3) * '0' + num
    else:
        num1 = num

    if len(num) % 4 != 0:
        num2 = (4 - len(num) % 4) * '0' + num
    else:
        num2 = num

    subresult1 = []
    subresult2 = []

    for i in range(0, len(num1), 3):
        subresult1.append(num1[i:i+3])

    for i in range(0, len(num2), 4):
        subresult2.append(num2[i:i+4])

    result1 = ''
    result2 = ''

    for i in subresult1:
        sub = i
        result = 0
        flag = 2
        for j in sub:
            result += int(j)*2**flag
            flag -= 1
        result1 += str(result)

    for i in subresult2:
        sub = i
        result = 0
        flag = 3
        for j in sub:
            result += int(j) * 2 ** flag
            flag -= 1
        if result == 10:
            result = 'A'
        elif result == 11:
            result = 'B'
        elif result == 12:
            result = 'C'
        elif result == 13:
            result = 'D'
        elif result == 14:
            result = 'E'
        elif result == 15:
            result = 'F'
        result2 += str(result)

    while result1[0] == '0':
        result1 = result1[1:]

    while result2[0] == '0':
        result2 = result2[1:]

    second.set(str(result1))
    third.set(str(result2))

def second_filled(text2):
    num = text2.get()
    subresult = []

    for i in num:
        subresult.append(i)

    result1 = ''

    for i in subresult:
        result = ''
        if i == '0':
            result = '000'
        elif i == '1':
            result = '001'
        elif i == '2':
            result = '010'
        elif i == '3':
            result = '011'
        elif i == '4':
            result = '100'
        elif i == '5':
            result = '101'
        elif i == '6':
            result = '110'
        elif i == '7':
            result = '111'
        result1 += str(result)

    while result1[0] == '0':
        result1 = result1[1:]

    first.set(str(result1))

    num = result1

    if len(num) % 4 != 0:
        num2 = (4 - len(num) % 4) * '0' + num
    else:
        num2 = num

    subresult2 = []

    for i in range(0, len(num2), 4):
        subresult2.append(num2[i:i+4])

    result2 = ''

    for i in subresult2:
        sub = i
        result = 0
        flag = 3
        for j in sub:
            result += int(j) * 2 ** flag
            flag -= 1
        if result == 10:
            result = 'A'
        elif result == 11:
            result = 'B'
        elif result == 12:
            result = 'C'
        elif result == 13:
            result = 'D'
        elif result == 14:
            result = 'E'
        elif result == 15:
            result = 'F'
        result2 += str(result)

    while result2[0] == '0':
        result2 = result2[1:]

    third.set(str(result2))

def third_filled(text3):
    num = text3.get()
    subresult = []

    for i in num:
        subresult.append(i)

    result1 = ''

    for i in subresult:
        result = ''
        if i == '0':
            result = '0000'
        elif i == '1':
            result = '0001'
        elif i == '2':
            result = '0010'
        elif i == '3':
            result = '0011'
        elif i == '4':
            result = '0100'
        elif i == '5':
            result = '0101'
        elif i == '6':
            result = '0110'
        elif i == '7':
            result = '0111'
        elif i == '8':
            result = '1000'
        elif i == '9':
            result = '1001'
        elif i == 'A':
            result = '1010'
        elif i == 'B':
            result = '1011'
        elif i == 'C':
            result = '1100'
        elif i == 'D':
            result = '1101'
        elif i == 'E':
            result = '1110'
        elif i == 'F':
            result = '1111'
        result1 += str(result)

    while result1[0] == '0':
        result1 = result1[1:]

    first.set(str(result1))

    num = result1

    if len(num) % 3 != 0:
        num1 = (3 - len(num) % 3) * '0' + num
    else:
        num1 = num

    subresult2 = []

    for i in range(0, len(num1), 3):
        subresult2.append(num1[i:i+3])

    result2 = ''

    for i in subresult2:
        sub = i
        result = 0
        flag = 2
        for j in sub:
            result += int(j)*2**flag
            flag -= 1
        result2 += str(result)

    while result2[0] == '0':
        result2 = result2[1:]

    second.set(str(result2))

root.mainloop()