import tkinter as tk

root = tk.Tk()
root.title('Tkinter Pack Layout')
root.geometry('600x400')

label1 = tk.Label(master=root, text='Tkinter',bg='red',fg='white')
label2 = tk.Label(master=root,text='Pack Layout',bg='green', fg='white')
label3 = tk.Label(master=root, text='Demo',bg='blue', fg='white')

label1.pack(side = tk.TOP, expand=True)
label2.pack(side=tk.TOP, expand=False)
label3.pack(side=tk.TOP, expand=False)

root.mainloop()