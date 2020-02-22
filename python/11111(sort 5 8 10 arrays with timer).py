from tkinter import *
import time
from tkinter import messagebox

def sort_array(sample):
    left = 0
    right = len(sample) - 1

    while left <= right:
        for i in range(left, right, +1):
            if sample[i] > sample[i + 1]:
                sample[i], sample[i + 1] = sample[i + 1], sample[i]
        right -= 1

        for i in range(right, left, -1):
            if sample[i - 1] > sample[i]:
                sample[i], sample[i - 1] = sample[i - 1], sample[i]
        left += 1
    return sample

def count_random(array):
    start_time = time.clock()
    sort_array(array)
    end_time = time.clock() - start_time
    return end_time

def count_reverse(array):
    sort_array(array)
    array.reverse()
    start_time = time.clock()
    sort_array(array)
    end_time = time.clock() - start_time
    return end_time

def count_straight(array):
    sort_array(array)
    start_time = time.clock()
    sort_array(array)
    end_time = time.clock() - start_time
    return end_time

root = Tk()
root.title('ЛАБА')
root.resizable(width = 'False', height = 'False')
root.geometry('500x220')

lbl2 = Label(text = 'Зависимость времени от длины и изначальной сортировки\n массива при сортировке методом шейкер', font = 'Times, 13')
lbl2.place(x = 5, y = 1)

lbl1 = Label(text = 'Порядок/Длина')
lbl1.place(x = 10, y = 45)

first_len_lbl = Label(text = '5 элементов')
first_len_lbl.place(x = 180, y = 45)

second_len_lbl = Label(text = '8 элементов')
second_len_lbl.place(x = 275, y = 45)

third_len_lbl = Label(text = '10 элементов')
third_len_lbl.place(x = 360, y = 45)

random_style_lbl = Label(text = 'Рандомная сортировка')
random_style_lbl.place(x = 10, y = 65)

reverse_style_lbl = Label(text = 'Сортировка по убыванию')
reverse_style_lbl.place(x = 10, y = 85)

straight_lbl = Label(text = 'Сортировка по возрастанию')
straight_lbl.place(x = 10, y = 105)

btn_result = Button(text = 'Построить таблицу', command = lambda: get_array(array1_entry,array2_entry, array3_entry))
btn_result.place(x = 185, y = 125)

scrollbar1 = Scrollbar(orient = HORIZONTAL)
scrollbar1.place(x = 10, y = 180)

array1_entry = Entry(xscrollcommand=scrollbar1.set)
array1_entry.place(x = 10, y = 155)

scrollbar1.config(command=array1_entry.xview)

scrollbar2 = Scrollbar(orient = HORIZONTAL)
scrollbar2.place(x = 180, y = 180)

array2_entry = Entry(xscrollcommand=scrollbar2.set)
array2_entry.place(x = 180, y = 155)

scrollbar2.config(command=array2_entry.xview)

scrollbar3 = Scrollbar(orient = HORIZONTAL)
scrollbar3.place(x = 330, y = 180)

array3_entry = Entry(xscrollcommand=scrollbar3.set)
array3_entry.place(x = 330, y = 155)

scrollbar3.config(command=array3_entry.xview)

def get_array(entry1, entry2, entry3):
    str1 = entry1.get()
    str2 = entry2.get()
    str3 = entry3.get()

    arr1 = str1.split(' ')
    arr2 = str2.split(' ')
    arr3 = str3.split(' ')

    if len(arr1) != 5 or len(arr2) != 8 or len(arr3) != 10:
        messagebox.showerror('Error 502', 'Проверьте правильность введённых данных!')

    else:
        first_random_lbl = Label(text='{:5.7f}'.format(count_random(arr1)))
        first_random_lbl.place(x=180, y=65)

        first_straight_lbl = Label(text='{:5.7f}'.format(count_straight(arr1)))
        first_straight_lbl.place(x=180, y=85)

        first_reverse_lbl = Label(text='{:5.7f}'.format(count_reverse(arr1)))
        first_reverse_lbl.place(x=180, y=105)

        second_random_lbl = Label(text='{:5.7f}'.format(count_random(arr2)))
        second_random_lbl.place(x=275, y=65)

        second_straight_lbl = Label(text='{:5.7f}'.format(count_straight(arr2)))
        second_straight_lbl.place(x=275, y=85)

        second_reverse_lbl = Label(text='{:5.7f}'.format(count_reverse(arr2)))
        second_reverse_lbl.place(x=275, y=105)

        third_random_lbl = Label(text='{:5.7f}'.format(count_random(arr3)))
        third_random_lbl.place(x=360, y=65)

        third_straight_lbl = Label(text='{:5.7f}'.format(count_straight(arr3)))
        third_straight_lbl.place(x=360, y=85)

        third_reverse_lbl = Label(text='{:5.7f}'.format(count_reverse(arr3)))
        third_reverse_lbl.place(x=360, y=105)

        result1 = Label(text = ' '.join(sort_array(arr1)))
        result1.place(x = 10, y = 195)

        result2 = Label(text = ' '.join(sort_array(arr2)))
        result2.place(x = 180, y = 195)

        result3 = Label(text = ' '.join(sort_array(arr3)))
        result3.place(x = 330, y = 195)

root.mainloop()