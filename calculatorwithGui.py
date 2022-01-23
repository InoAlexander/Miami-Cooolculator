from tkinter import *
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
window.geometry("600 x 500")
window.minsize(600,650)
window.maxsize(600, 650)
window.config(bg="gray")
window.title("Inos 'Coolculator' ")
icon = image(file = '')
window.photoicon(false, icon) 

scvalue.StringVar()
scvalue.set("")
f = Frame(window, padx=15, pady=15)
screen = Entry(f, textvar = scvalue, font = "lucida 50 bold",
bg = "light blue")
screen.pack(fill = X, padx = 15, pady = 15)
f.pack()

