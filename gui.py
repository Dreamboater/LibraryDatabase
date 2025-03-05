from tkinter import *
from tkinter import ttk
root = Tk()
root.minsize(400,500)
frm = ttk.Frame(root)
frm.grid()
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=0)
ttk.Label(frm, text="Library Database").grid(column=0, row=0)
ttk.Combobox(frm)

root.mainloop()