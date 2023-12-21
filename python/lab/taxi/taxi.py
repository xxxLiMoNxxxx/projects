import tkinter as tk
from tkinter import *
from tkinter import messagebox

classes = []

def clear_screen_and_message(selection):
    # Очистка екрана
    label_quastion.pack_forget()
    label_money.pack_forget()
    button_money.pack_forget()
    label_card.pack_forget()
    button_card.pack_forget()

    # Отображение сообщения и индикатора загрузки
    message = f"Отлично! Вы выбрали: {selection}, подождите..."
    loading_label = tk.Label(root, text=message, font="Arial 14", foreground="black", bg="#f5da56")
    loading_label.place(relx=0.5, rely=0.4, anchor="center")

    # Создание и отображение индикатора прогресса
    progress_bar = tk.Canvas(root, width=200, height=20, bg="white")
    progress_bar.place(relx=0.5, rely=0.5, anchor="center")

    # Имитация загрузки через изменение длины прямоугольника
    progress = 0
    increment = 5
    end_progress = 200
    animate_loading(progress_bar, progress, end_progress, increment, loading_label)

def animate_loading(canvas, progress, end_progress, increment, label):
    if progress < end_progress:
        canvas.create_rectangle(0, 0, progress, 20, fill="blue", width=0)
        progress += increment
        root.after(50, lambda: animate_loading(canvas, progress, end_progress, increment, label))
    else:
        label.place_forget()
        canvas.place_forget()
        messagebox.showinfo("Готово!", "Операція завершена")
        choose_classes_window()

def money_button_clicked():
    clear_screen_and_message("Готівка")

def card_button_clicked():
    clear_screen_and_message("Карта")

def add_class(class_name):
    global classes
    if class_name not in classes:
        classes.append(class_name)
        selected_classes.set(f"Обрані класи: {', '.join(classes)}")

def choose_classes_window():
    label_quastion.config(text="Оберіть клас таксі:")
    label_quastion.pack()

    tkinter_label = tk.Label(root, text="Це перероблено з консолі в Tkinter", font="Arial 10 italic", foreground="black", bg="#f5da56")
    tkinter_label.pack()

    buttons_frame = tk.Frame(root, bg="#f5da56")
    buttons_frame.pack()

    buttons = []
    taxi_classes = ['Економ', 'Середній', 'Бізнес']
    for taxi_class in taxi_classes:
        button = tk.Button(buttons_frame, text=f"{taxi_class}", font="Arial 13", command=lambda class_name=taxi_class: add_class(class_name))
        button.pack(side=tk.TOP)
        buttons.append(button)

    selected_classes.set("Обрані класи:")
    result_label.config(textvariable=selected_classes)
    result_label.pack()

root = tk.Tk()

root.geometry("720x1280")
root.minsize(50, 50)
root.resizable(False, False)
root.title("Застосунок")
root.configure(bg="#f5da56")

img_money = PhotoImage(file='python/lab/taxi/money.png')
img_card = PhotoImage(file='python/lab/taxi/card.png')

label_quastion = tk.Label(root, text="Яку ви хочете обрати форму оплати", font="Arial 20", foreground="black", bg="#f5da56")
label_money = tk.Label(root, text="Готівка", font="Arial 13", foreground="black", bg="#f5da56")
button_money = tk.Button(root, command=money_button_clicked)
button_money.image = img_money
button_money['image'] = button_money.image
label_card = tk.Label(root, text="Карта", font="Arial 13", foreground="black", bg="#f5da56")
button_card = tk.Button(root, command=card_button_clicked)
button_card.image = img_card
button_card['image'] = button_card.image

selected_classes = tk.StringVar()
result_label = tk.Label(root, font="Arial 13", foreground="black", bg="#f5da56")

label_quastion.pack()
label_money.pack()
button_money.pack()
label_card.pack()
button_card.pack()

root.mainloop()
