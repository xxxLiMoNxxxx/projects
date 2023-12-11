import tkinter as tk
from tkinter import messagebox
import random

root = tk.Tk()
random_number = random.randint(1, 10)

def random():
    user_number = int(entry.get())
    error = "Ви не вгадали"
    if user_number == random_number:
        messagebox.showinfo("Ви вгадали!", "Ви вгадали")
    elif user_number > 10:
        messagebox.showwarning("warning", "Ви пишите число завелике, треба від 1 до 10!")
    elif user_number < 1:
        messagebox.showwarning("warning", "Ви пишите число замале, треба від 1 до 10!")
    elif user_number > random_number:
        messagebox.showwarning("Інформація", "Ваше число більше ніж загадане!")
    elif user_number < random_number:
        messagebox.showwarning("Інформація", "Ваше число менше ніж загадане!")
    else:
        messagebox.showerror("Ви не вгадали", error)

root.geometry("400x200")
root.minsize(50, 50)
root.resizable(False, False)
root.title("Застосунок")

label = tk.Label(root, text="Вгадайте число від 1 до 10", font="Arial 12", foreground="black")
entry = tk.Entry(root)
button = tk.Button(root, text="ок", command=random)

label.pack()
entry.pack()
button.pack()

root.mainloop()