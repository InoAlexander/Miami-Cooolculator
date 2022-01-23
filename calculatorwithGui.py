from pickle import GLOBAL
from tkinter import *
from PIL import Image, ImageTk

global scvalue

#operations in the calculator
def click(event):
    
    global scvalue
    text = event.widget.cget("text")
    if text == '=':
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            value = eval(screen.get())

        scvalue.set(value)
        screen.update()
    elif text == 'C':
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get()+text)
    screen.update()
    
# window sizing for calculator gui 

window = Tk()
window.geometry("600x650")
window.minsize(600,650)
window.maxsize(600, 650)
window.config(bg="aliceblue")
window.title("Inos 'Coolculator' ")
icon = ImageTk.PhotoImage(Image.open('sexy_ayanami.png'))
window.iconphoto(False, icon) 


scvalue = StringVar()
scvalue.set("")
f = Frame(window, bg="yellow", padx=10, pady=10)
screen = Entry(f, textvar = scvalue, font = "lucida 50 bold",
bg = "light blue")
screen.pack(fill = X, padx = 15, pady = 15)
f.pack()

# option rows
options1 = ["7", "8", "9", "+"]
options2 = ["4", "5", "6", "-"]
options3 = ["1", "2", "3", "*"]
options4 = ["0", "C", "=", "/"]

f = Frame(window, bg="cyan", padx = 25, pady = 25)
for i in options1:
    b = Button(f, text = i, padx=10, pady=10, font="lucida 25 bold")
    b.pack(side=LEFT, padx = 10, pady=10)
    b.bind("<Button-1>", click)
f.pack()

f = Frame(window, bg="magenta", padx=25, pady=25)
for i in options2:
    b = Button(f, text=i, padx=10, pady=10, font = "lucida 25 bold")
    b.pack(side=LEFT, padx=10, pady=10)
    b.bind("<Button-1>", click)
f.pack()

f = Frame(window, bg="purple", padx=25, pady=25)
for i in options3:
    b = Button(f, text=i, padx=10, pady=10, font = "lucida 25 bold")
    b.pack(side=LEFT, padx=10, pady=10)
    b.bind("<Button-1>", click)
f.pack()

f = Frame(window, bg="gray", padx=25, pady=25)
for i in options4:
    b = Button(f, text=i, padx=10, pady=10, font = "lucida 25 bold")
    b.pack(side=LEFT, padx=10, pady=10)
    b.bind("<Button-1>", click)
f.pack()

window.mainloop()
