import tkinter as tk
from tkinter import messagebox
from tkinter import *

root = tk.Tk()

def show_message():
    user_email = entry_email.get()
    user_name = entry_name.get()
    user_pass = entry_pass.get()
    user_copy_pass = entry_copy_pass.get()
    error_email = "Ви не ввели email!"
    error_name = "Ви не ввели логин!"
    error_pass = "Ви не ввели пароль!"
    if user_email == "":
        messagebox.showerror("Помилка", error_email)
    elif user_name == "":
        messagebox.showerror("Помилка", error_name)
    elif user_pass == "":
        messagebox.showerror("Помилка", error_pass)
    elif user_pass != user_copy_pass:
        messagebox.showerror("Помилка", "Ви ввели різні паролі")
    else:
        messagebox.showinfo("Повідомлення", "Ви успішно зарееструвалися!")

def cancel_command():
    entry_email.delete(0, END)
    entry_name.delete(0, END)
    entry_pass.delete(0, END)
    entry_copy_pass.delete(0, END)

root.geometry("800x600")
root.minsize(50, 50)
root.resizable(False, False)
root.title("Застосунок")
root.iconbitmap("projects_python\lab\ico.ico")

label_email = tk.Label(root, text="Введіть свій email", font="Arial 12", foreground="black")
entry_email = tk.Entry(root)
label_name = tk.Label(root, text="Введіть свій логин", font="Arial 12", foreground="black")
entry_name = tk.Entry(root)
label_pass = tk.Label(root, text="Введіть свій пароль", font="Arial 12", foreground="black")
entry_pass = tk.Entry(root)
label_copy_pass = tk.Label(root, text="Повторить пароль", font="Arial 12", foreground="black")
entry_copy_pass = tk.Entry(root)
button = tk.Button(root, text="ок", command=show_message)
button_cancel = tk.Button(root, text="скасувати", command=cancel_command)

label_email.pack()
entry_email.pack()
label_name.pack()
entry_name.pack()
label_pass.pack()
entry_pass.pack()
label_copy_pass.pack()
entry_copy_pass.pack()
button.pack()
button_cancel.pack()

root.mainloop()