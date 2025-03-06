import tkinter as tk
from tkinter import ttk

# root window
root = tk.Tk()
root.geometry("600x400")
root.title('Library Database')
root.resizable(0, 0)
root.iconbitmap("myIcon.ico")

# configure the grid
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)


# Title
title_label = ttk.Label(root, text="Title:")
title_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

title_entry = ttk.Entry(root)
title_entry.grid(column=1, row=0, sticky=tk.W, padx=5, pady=5)

# Author
author_label = ttk.Label(root, text="Author:")
author_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

author_entry = ttk.Entry(root,  show="*")
author_entry.grid(column=1, row=1, sticky=tk.W, padx=5, pady=5)

# ISBN
isbn_label = ttk.Label(root, text="ISBN:")
isbn_label.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)

isbn_entry = ttk.Entry(root,  show="*")
isbn_entry.grid(column=1, row=2, sticky=tk.W, padx=5, pady=5)

# login button
login_button = ttk.Button(root, text="Login")
login_button.grid(column=1, row=3, sticky=tk.W, padx=5, pady=5)


root.mainloop()
