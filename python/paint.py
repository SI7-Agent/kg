from tkinter import *
from tkinter.colorchooser import *
from tkinter import filedialog, messagebox


class Paint(Frame):
    def __init__(self, parent):

        Frame.__init__(self, parent)

        self.parent = parent
        self.color = 'black'
        self.brush_size = 2
        self.line_start = None

        self.setUI()

        self.canv.bind('<B1-Motion>', self.draw)

        self.parent.iconbitmap(r'C:\Users\kiril\OneDrive\Pictures\paint.ico')

        self.canv.bind('<ButtonRelease-1>', self.counter1)

    def del_canv(self, event):

        self.canv.delete('all')

    def rubber(self, event):

        self.color = 'white'
        self.canv.create_oval(event.x - self.brush_size,
                              event.y - self.brush_size,
                              event.x + self.brush_size,
                              event.y + self.brush_size,
                              fill = self.color, outline = self.color, tag = 'group' + str(self.draw_counter))

    def GetColor(self):

        color0 = askcolor()
        color0 = color0[1]
        self.color = color0

    def set_brush_size(self, new_size):

        self.brush_size = new_size

    def text(self):

        count = 0

        global add_btn
        global words_label
        global font_size
        global fonts
        global scrl
        global cancel_btn

        def get_cor(event):

            global x
            global y

            x = event.x
            y = event.y

        self.canv.bind('<Button-1>', get_cor)

        scrl = Scrollbar(self, orient = HORIZONTAL)
        scrl.grid(row = 2, column = 8, columnspan = 1)

        words = StringVar(self)
        words_label = Entry(self, textvariable = words, width = 24, xscrollcommand = scrl.set)
        words_label.grid(column = 7, row = 1, columnspan = 2)

        scrl.config(command = words_label.xview)

        font_size = Scale(self, from_ = 1, to = 50, orient = HORIZONTAL, width = 7, sliderlength = 20, label = 'Размер шрифта')
        font_size.grid(column = 8, row = 0, rowspan = 2, columnspan = 4)
        font_size.set(20)

        font = StringVar(self)
        font.set('Arial')

        fonts = OptionMenu(self, font, 'Arial', 'Courier', 'Fixedsys', 'Symbol', 'Times', 'Verdana')
        fonts.grid(row = 2, column = 9)

        cancel_btn = Button(self, text = 'Отмена', command = lambda: self.destroy_text_widget(), width = 8)
        cancel_btn.grid(row = 2, column = 11)

        def create_t():

            try:

                self.canv.create_text(x, y, text = words.get(), fill = self.color, font = (font.get(), font_size.get()),
                                      tag = 'group' + str(self.draw_counter - 1))

            except:

                messagebox.showerror('Ошибка', 'Не указано место вставки текста\nПеред нажатием на кнопку щелкните в нужное место.')

            self.destroy_text_widget()

        def create_t_combo(event):

            try:

                self.canv.create_text(x, y, text = words.get(), fill = self.color, font = (font.get(), font_size.get()),
                                      tag = 'group' + str(self.draw_counter - 1))

            except:

                messagebox.showerror('Ошибка', 'Не указано место вставки текста\nПеред нажатием на кнопку щелкните в нужное место.')

            self.destroy_text_widget()

        add_btn = Button(self, text = 'Добавить', command = lambda: create_t())
        add_btn.grid(row = 2, column = 10)

        self.parent.bind('<Return>', create_t_combo)

        count += 1

    def destroy_text_widget(self):

        self.parent.unbind('<Return>')

        add_btn.destroy()
        words_label.destroy()
        font_size.destroy()
        fonts.destroy()
        scrl.destroy()
        cancel_btn.destroy()

    def draw(self, event):

        self.canv.create_oval(event.x - self.brush_size,
                              event.y - self.brush_size,
                              event.x + self.brush_size,
                              event.y + self.brush_size,
                              fill = self.color, outline = self.color, tag = 'group' + str(self.draw_counter))
        print(self.color)

    def draw_lines(self, x, y, brush_size, col):

        if self.line_start:

            x_origin, y_origin = self.line_start

            self.canv.create_line(x_origin, y_origin, x, y, width = brush_size, fill = col,
                                  tag = 'group' + str(self.draw_counter))
            self.line_start = None

        else:

            self.line_start = (x, y)

    def save_pic_combo(self, event):

        self.canv.update()
        filename = filedialog.asksaveasfilename(filetypes = [('Все файлы', '*'), ('Файлы изображений', '*.ps')],
                                                defaultextension = '.ps', title = 'Расположение и название')
        self.canv.postscript(file = filename)

    def save_pic(self):

        self.canv.update()
        filename = filedialog.asksaveasfilename(filetypes = [('Все файлы', '*'), ('Файлы изображений', '*.ps')],
                                                defaultextension = '.ps', title = 'Расположение и название')
        self.canv.postscript(file = filename)

    def destroy_paint(self, event):

        result = messagebox.askyesno('Внимание!', 'Вы собираетесь закрыть программу\nХотите сохранить несохранённые данные?')

        if result == True:

            self.save_pic()
            self.parent.destroy()

        else:

            self.parent.destroy()

    def ctrl_z(self, event):

        self.canv.delete('group' + str(self.draw_counter - 1))

        self.canv.update()

        if self.draw_counter > 0:

            self.draw_counter -= 1

    def counter1(self, event):

        self.draw_counter += 1

    draw_counter = 0

    def setUI(self):

        self.parent.bind('<Alt-BackSpace>', self.del_canv)
        self.parent.bind('<Control-z>', self.ctrl_z)
        self.parent.bind('<Alt-F4>', self.destroy_paint)
        self.parent.bind('<Control-s>', self.save_pic_combo)

        self.parent.title('Рисовалка')
        self.pack(fill = BOTH, expand = 1)

        self.columnconfigure(11, weight = 3)
        self.rowconfigure(4, weight = 2)

        self.canv = Canvas(self, bg = 'white', cursor = 'pencil')
        self.canv.grid(row = 4, column = 0, columnspan = 27, padx = 5, pady = 5, sticky = E + W + S + N)

        color_lab = Label(self, text = 'Цвет: ')
        color_lab.grid(row = 0, column = 6, padx = 6)

        color_choose_btn = Button(self, text = 'Выбрать цвет', width = 12, command = lambda: self.GetColor(),
                                  cursor = 'spraycan')
        color_choose_btn.grid(row = 0, column = 7, pady = 1)

        clear_btn = Button(self, text = 'Очистить холст', width = 12, command = lambda: self.canv.delete('all'))
        clear_btn.grid(row = 0, column = 8, pady = 1)

        size_lab = Label(self, text = 'Размер кисти: ')
        size_lab.grid(row = 0, column = 0, padx = 5)

        one_btn = Button(self, text = '2px', width = 7, command = lambda: self.set_brush_size(2))
        one_btn.grid(row = 0, column = 1, pady = 1)

        two_btn = Button(self, text = '5px', width = 7, command = lambda: self.set_brush_size(5))
        two_btn.grid(row = 0, column = 2, pady = 1)

        five_btn = Button(self, text = '7px', width = 7, command = lambda: self.set_brush_size(7))
        five_btn.grid(row = 0, column = 3, pady = 1)

        seven_btn = Button(self, text = '10px', width = 7, command = lambda: self.set_brush_size(10))
        seven_btn.grid(row = 1, column = 1)

        ten_btn = Button(self, text = '20px', width = 7, command = lambda: self.set_brush_size(20))
        ten_btn.grid(row = 1, column = 2)

        twenty_btn = Button(self, text = '50px', width = 7, command = lambda: self.set_brush_size(50))
        twenty_btn.grid(row = 1, column = 3)

        save_btn = Button(self, text = 'Сохранить', command = lambda: self.save_pic(), width=12)
        save_btn.grid(row = 2, column = 7)

        drawing_lab = Label(self, text = 'Рисование: ')
        drawing_lab.grid(row = 2, column = 0, padx = 5)

        default_btn = Button(self, text = 'Стандарт', width = 7,
                             command = lambda: self.canv.bind('<B1-Motion>', self.draw, self.canv.unbind('<Button-1>')))
        default_btn.grid(row = 2, column = 1, pady = 1)

        lines_btn = Button(self, text = 'Прямые', width = 7, command = lambda: self.canv.bind("<Button-1>",
                                                                                              lambda e: self.draw_lines(e.x, e.y, self.brush_size, self.color), self.canv.unbind('<B1-Motion>')))
        lines_btn.grid(row = 2, column = 2, pady = 1)

        rubber_btn = Button(self, text = 'Ластик', width = 7,
                            command = lambda: self.canv.bind('<B1-Motion>', self.rubber, self.canv.unbind('<Button-1>')))
        rubber_btn.grid(row = 2, column = 4, pady = 1)

        text_btn = Button(self, text = 'Надпись', width = 7, command = lambda: self.text())
        text_btn.grid(row = 2, column = 3, pady = 1)


def main():

    root = Tk()
    root.geometry('850x600')
    root.resizable(width = False, height = False)
    root = Paint(root)
    root.mainloop()

if __name__ == '__main__':

    main()