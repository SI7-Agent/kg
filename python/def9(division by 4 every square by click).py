from tkinter import *

i  = 1

def split_sqrt():

    global i
    i *= 2
    g = 0
    while g <= 200 - 200/i:
        g = g + 200/i
        canv.create_line(3, g, 200, g)
        canv.create_line(g, 3, g, 200)


root = Tk()
canv = Canvas(bg = 'white')
canv.grid(sticky = 'nw')
root.rowconfigure(2, weight = 1)
root.columnconfigure(2, weight = 1)
canv.create_rectangle(3, 200, 200, 3, outline = 'black')
root.geometry('450x300')
root.resizable(width = False, height = False)

split_btn = Button(text = 'Split', width = 5, command = lambda: split_sqrt())
split_btn.grid(row = 2, column = 1)

root.mainloop()