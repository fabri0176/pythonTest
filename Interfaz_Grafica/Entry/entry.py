from tkinter import *

root = Tk()

label = Label(root, text="Nombre Completo")
label.grid(row=0,column=0,sticky="w",padx=5,pady=2)

entry = Entry(root)
entry.grid(row=0,column=1,padx=5,pady=2)
entry.config(justify="right",state="normal")

label2 = Label(root, text="Apellidos")
label2.grid(row=1,column=0,sticky="w",padx=5,pady=2)

entry2 = Entry(root)
entry2.grid(row=1,column=1,padx=5,pady=2)


label3 = Label(root, text="Contraseña")
label3.grid(row=2,column=0,sticky="w",padx=5,pady=2)

entry3 = Entry(root)
entry3.grid(row=2,column=1,padx=5,pady=2)
entry3.config(show="*")


root.mainloop()