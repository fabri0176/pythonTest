try:
    # for Python2
    from Tkinter import *
except ImportError:
    # for Python3
    from tkinter import *

root = Tk()

root.title("Hola mundo")
root.resizable(1,1)
# root.iconbitmap("hola.ico")


#Abajo del todo
root.mainloop()