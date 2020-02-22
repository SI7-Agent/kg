from tkinter import *

root = Tk()
root.title('DEF11')
root.resizable(width = 'false', height = 'false')
root.geometry('500x100')

num_entry = Entry()
num_entry.place(x = 10, y = 50)

result_lbl = Label(bg = 'white', width = 20)
result_lbl.place(x = 200, y = 50)

btn = Button(text = 'Решить', command = lambda: trans(num_entry, result_lbl))
btn.place(x = 200, y = 10)

def trans(entry, lbl):
    num = entry.get()
    if '.' in num:
        pass
    else:
        num += '.'

    flag = ''

    if '-' in num:
        flag = 1
        num = num[1:]
    else:
        num = num
        flag = 0

    arr = num.split('.')

    num1 = int(arr[0])
    arr2 = []
    while int(num1) > 0:
        arr2.append(int(num1)%5)
        num1 /= 5

    arr2.reverse()
    int_part = ''.join(map(str, arr2))

    arr3 = []
    num2 = ''
    if arr[1] != '':
        num2 = '0.' + arr[1]
        i = 0
        while i < 8:
            num2 = str(float(num2)*5)
            arr3.append(num2[0])
            num2 = str(float(num2) - float(num2[0]))
            i += 1
    else:
        num2 = '0'
        arr3.append(num2)

    float_part = ''.join(map(str, arr3))
    num_ready = ''
    if flag == 0:
        num_ready = int_part + '.' + float_part
    elif flag == 1:
        num_ready = '-' + int_part + '.' + float_part

    lbl.destroy()
    if entry.get() == '0':
        result_lbl = Label(text='0', bg='white', width=20)
        result_lbl.place(x=200, y=50)
    else:
        result_lbl = Label(text = num_ready, bg='white', width=20)
        result_lbl.place(x=200, y=50)

root.mainloop()