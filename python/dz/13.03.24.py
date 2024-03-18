from tkinter import *

def buttonl_click():
    root.geometry ('800x400')
    root['bg'] = 'green'
    buttonl ['width'] = 30
    buttonl['bg'] = 'blue'
    buttonl['fg'] = 'white'
    buttonl['state'] = 'disable'
    button2 ['width'] = button2 ['width'] + 5

def mouse_move (event) :
    label['bg'] = 'red'
    label['width'] = 40
    label['height'] = label['height'] + 5
    label['fg'] = 'yellow'
    label ['text'] = 'Ми вивчаемо мову програмування Python!'

root = Tk ()
root.geometry ('400x300')

buttonl = Button (text = 'BikHO npoekry', width = 20, height = 2, bg = 'grey', fg = 'yellow', command = buttonl_click)
button2 = Button (text = 'Напис', width = 10, height = 3, bg = 'blue', fg = 'white')
label = Label (text = '8 клас', fg = 'blue', font = 'Arial 14')

buttonl.pack ()
button2.pack ()
label.pack ()

button2.bind ('<Motion>', mouse_move)

root.mainloop()