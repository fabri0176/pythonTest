from tkinter import *

root = Tk()

# String vars
texto = StringVar()
texto.set("Un nuevo texto")

label = Label(root,text="Otra etiqueta")
label.pack(anchor="center")
label.config(bg="green",fg="blue",font="Verdana")
label.config(textvariable=texto)

image = PhotoImage(file="images/image")
Label(root, image=image,bd=0).pack(side="left")

root.mainloop()
