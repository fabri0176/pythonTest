from tkinter import *

# Configuración raiz
root = Tk()
root.title("Hola Mundo")
root.resizable(1,1)
root.iconbitmap('favicon.ico')

frame = Frame(root)
frame.pack(fill='both',expand=1)
frame.config(cursor="arrow",width=480,height=320)
frame.config(bg="blue")
frame.config(bd=25)
frame.config(relief="sunken")
root.config(bg="green")
root.mainloop()