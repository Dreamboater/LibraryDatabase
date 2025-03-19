import tkinter as tk
from tkinter import ttk

# root window
root = tk.Tk()
root.geometry("300x400")
root.resizable(True,True)
root.title('Library Database')
root.resizable(1, 1)
root.iconbitmap("myIcon.ico")

# configure the grid
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

# load the database
file_list = [] # create a temp list to work with until saving

file = open('database.txt', 'r')
for line in file:   # load in the file to the temp list
    file_list.append(line)
file.close()

paddingx = 50

# Title
title_label = ttk.Label(root, text="Title:")
title_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

title_entry = ttk.Entry(root)
title_entry.grid(column=0, row=0, sticky=tk.W, padx=paddingx, pady=5)

# Author
author_label = ttk.Label(root, text="Author:")
author_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

author_entry = ttk.Entry(root)
author_entry.grid(column=0, row=1, sticky=tk.W, padx=paddingx, pady=5)

# ISBN
isbn_label = ttk.Label(root, text="ISBN:")
isbn_label.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)

isbn_entry = ttk.Entry(root)
isbn_entry.grid(column=0, row=2, sticky=tk.W, padx=paddingx, pady=5)
def add_entry():
    entry = title_entry.get()+","+author_entry.get()+","+isbn_entry.get()
    file_list.append(entry)
    print(file_list)

# add button
add_button = ttk.Button(root, text="Add", command =lambda: add_entry())
add_button.grid(column=0, row=3, sticky=tk.W, padx=100, pady=5)

def save_entry():
    file = open('database.txt', 'w')
    for item in file_list:
        file.write(item)
    file.close()

# save button
save_button = ttk.Button(root, text="Save", command =lambda: save_entry())
save_button.grid(column=0, row=4, sticky=tk.W, padx=100, pady=5)
# add functionality of the buttons


root.mainloop()
