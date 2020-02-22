# Назначение: на ведённых точках построить прямоугольник с наибольшим периметром,
#             где точки - вершины прямоугольника
#
# mas - основной массив, в котором содержатся все координаты точек
# l - вспомогательный массив, в котором содержатся изменённые коордиаты точек
# max1 - максимальный периметр прямоугольника
# i,k,g,j - счётчики
# a,b,c,d,ab,bc,cd,da - стороны промоугольника
# p - периметр рассматриваемого прямоугольника
# e - прямоугольник,нарисованный в canvas
# x,y - координаты точки
# label_x,label_y - текст в главном окне 
# entry_x,entry_y - ввод координат точек
# okno - главное окно
# max_x,max_y,min_x,min_y - максимальные значения по х и у

from tkinter import *
from proverka import check
from tkinter import messagebox
from math import sqrt

mas = []
i = [0]
max1 = 0
e = ''

# Нахождение угла между прямыми
def ugol(x,y):
    l = (abs(x[0]*y[0]+x[1]*y[1]))/(sqrt(x[0]**2+x[1]**2)*sqrt(y[0]**2+y[1]**2))
    return l

# Нахождение периметра
def perimetr(a,b,c,d):
    sum1 = sqrt(a[0]**2+a[1]**2)+sqrt(b[0]**2+b[1]**2)+sqrt(c[0]**2+c[1]**2)\
           +sqrt(d[0]**2+d[1]**2)
    return sum1

# Построение точек, прямоугольника, масштабирование
def tochka(x,y):
    global max1
    global e
    global t
    l = []
    # Проверка
    a = check(x)
    b = check(y)
    if a == 0 and b == 0 and len(x)>0 and len(y)>0:
        x = float(x)
        y = float(y)
        if [x,y] in mas:
            messagebox.showerror("Ошибка!", "Введите неповторяющиеся точки")
        else:
            mas.append([])
            mas[i[0]].append(x)
            mas[i[0]].append(y)
            i[0]+=1
            text_1.delete(1.0,END)

            # Заполнение текстового поля
            for k in range(1,i[0]+1):
                s = str(mas[k-1])
                if k<=9:
                    text_1.insert(float(str(k)+'.0'),str(k)+'.  '+s[1:-1]+'\n')
                else:
                    text_1.insert(float(str(k)+'.0'),str(k)+'. '+s[1:-1]+'\n')
                    
            # Создание вспомогательного массива        
            for k in range(len(mas)):
                l.append(mas[k][:])
            for k in range(len(l)):
                l[k][0]+=200
                l[k][1]=-l[k][1]+200

            # Масштабирование
            if len(l)>=2:
                max_x = -9999999999
                max_y = -9999999999
                min_x = 9999999999
                min_y = 9999999999
                canvas.delete('all')
                canvas.create_rectangle(3,3,401,401,width=2,outline='black')
                for k in range(len(l)):
                    if l[k][0] > max_x:
                        max_x = l[k][0]
                    if l[k][1] > max_y:
                        max_y = l[k][1]
                    if l[k][0] < min_x:
                        min_x = l[k][0]
                    if l[k][1] < min_y:
                        min_y = l[k][1]
                if max_x-min_x > max_y-min_y: raz = max_x-min_x
                else: raz = max_y-min_y
                raz /= 20
                max_x += raz 
                max_y += raz
                min_x -= raz
                min_y -= raz
                if max_x-min_x > max_y-min_y: a = max_x-min_x
                else: a = max_y-min_y
                for k in range (len(l)):
                    l[k][0] = (l[k][0] - min_x)/a*400
                    l[k][1] = (l[k][1] - min_y)/a*400
            
            for k in range(len(l)):
                canvas.create_oval(l[k][0],l[k][1],l[k][0],l[k][1],\
                                   fill ='black', width = 2)
            # Постороение прямоугольника
            if len(l)>=4:
                for k in range(len(l)):
                    for g in range(len(l)):
                        for j in range(len(l)):
                            for m in range(len(l)):
                                if k != g and k!= j and k!=m and g!=j and g!=m\
                                   and j!=m:
                                    ab = [mas[k][0]-mas[g][0],mas[k][1]-mas[g][1]]
                                    bc = [mas[g][0]-mas[j][0],mas[g][1]-mas[j][1]]
                                    cd = [mas[j][0]-mas[m][0],mas[j][1]-mas[m][1]]
                                    da = [mas[m][0]-mas[k][0],mas[m][1]-mas[k][1]]
                                    p = perimetr(ab,bc,cd,da)
                                    if ugol(ab,bc)==0 and ugol(bc,cd)==0 \
                                       and ugol(cd,da)==0 and ugol(da,ab) ==0\
                                       and p>=max1:
                                        canvas.delete(e)
                                        e = canvas.create_line(l[k][0],l[k][1],\
                                        l[g][0],l[g][1],l[j][0],l[j][1],l[m][0],\
                                        l[m][1],l[k][0],l[k][1], width= 2)
                                        max1 = p                                                           
    else:
        messagebox.showerror("Ошибка!", "Введите правильные координаты точек")
    entry_x.delete(0,END)
    entry_y.delete(0,END)        

okno = Tk()
okno.title('')
okno.geometry('700x415')

canvas = Canvas(width = 400,height = 400,bg = 'white')
canvas.grid(sticky = 'nw')

label_x = Label(text = 'Координата точки по X:')
label_x.place(x = 420,y = 10)
label_y = Label(text = 'Координата точки по Y:')
label_y.place(x = 420, y = 40)

entry_x = Entry(width = 5)
entry_x.place(x = 580,y = 9)
entry_y = Entry(width = 5)
entry_y.place(x=580,y = 37)

button = Button(text = 'Ввод',width = 10)
button.place(x = 557, y = 65)
button.bind('<Button-1>', lambda event:tochka(entry_x.get(),entry_y.get()))
okno.bind('<Return>', lambda event:tochka(entry_x.get(),entry_y.get()))

scrollbar = Scrollbar(okno)
scrollbar.place(x=650,y = 130,width = 25,height = 280)
text_1 = Text(okno,width = 25, height = 17,yscrollcommand = scrollbar.set)
scrollbar.config(command = text_1.yview)
label_1 = Label(text= 'Координаты ввёденных точек:')
label_1.place(x = 465,y = 97)
text_1.place(x = 450, y = 120)

canvas.create_rectangle(3,3,401,401,width=2,outline='black')

okno.mainloop()
