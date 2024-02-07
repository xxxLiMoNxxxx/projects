import tkinter as tk

def click():
    label4.config(text="dsfgrftgyuthgucx fdtgrskl.;mcgbbvcm")

def button(event):
    global font_size
    font_size += 5
    label4.config(font=f"Arial {font_size}")
def button_minus(event):
    global font_size
    font_size -= 5
    label4.config(font=f"Arial {font_size}")
def del_all(event):
    for widget in root.winfo_children(): 
        widget.destroy() 
def hover_text(event):
    global text_color
    text_color = "red"
    label2.config(fg=f"{text_color}")
def hover_text_none(event):
    global text_color
    text_color = "black"
    label2.config(fg=f"{text_color}")

font_size = 10
text_color = "black"
root = tk.Tk()

root.geometry("720x1280")
root.title("fdgdfgdfg")

label4 = tk.Label(root, text="dfhgfdjhjghghkghk")
button4 = tk.Button(root, text="gfdfdhdfh", command=click)
label2 = tk.Label(root, text="dfhgfdjhjghghkghk", fg='black', font="Arial 15")

button4.bind("<Button-1>", button)
button4.bind("<Button-3>", button_minus)
label2.bind("<Enter>", hover_text)
label2.bind("<Leave>", hover_text_none)
root.bind("<F2>", del_all)
label4.pack()
button4.pack()
label2.pack()

root.mainloop()