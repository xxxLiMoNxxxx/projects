from tkinter import *
from tkinter.messagebox import *

def click(event):
    root['bg'] = 'red'
    w = root.winfo_width ()+300
    x = root.winfo_x()-50
    root.geometry('{}x100+{}+200' . format (w, x) )
    showinfo ('', 'Ми вивчаемо програмування!')

def key_press(event):
    root['bg'] = 'blue'
    x = root.winfo_x ()
    y = root.winfo_y() + 300
    w = root.winfo_width ()+200
    root.geometry('{}x100+{}+{}' . format (w, x, y) )

root = Tk()

root.geometry('200x100+150+100')
root.title("Практична робота")
root['bg'] = 'grey'

root.bind('<1>', click)
root.bind('<KeyPress>', key_press)

root.mainloop()