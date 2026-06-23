import tkinter as tk
from tkinter import ttk
window=tk.Tk()
window.geometry("400x300")
window.title("scale widget,spinbox,menu")
def displayvalue(value):
    print(value)
scale=ttk.Scale(window,from_=0 , to =500, length =300, value=150,command=displayvalue,orient="horizontal")
scale.pack()
spinbox=ttk.Spinbox(window,from_=0, to=100,command=lambda:print(spinbox.get()))
spinbox.pack()
#cretare menu bar 
menubar=tk.Menu(window)
window.config(menu=menubar)
#file menu 
file_menu=tk.Menu(menubar,tearoff=False)
menubar.add_cascade(label="file",menu=file_menu)
file_menu.add_command(label="new",command=print("new menu"))
file_menu.add_command(label="open",command=lambda:print("open menu "))
file_menu.add_command(label="save",command=lambda:print("save menu "))
file_menu.add_separator()
file_menu.add_command(label="exit",command=lambda:print("exit menu"))



#edit menu 
edit_menu=tk.Menu(menubar,tearoff=False)
menubar.add_cascade(label="edit",menu=edit_menu)
edit_menu.add_command(label="cut",command=print("new menu"))
edit_menu.add_command(label="copy",command=lambda:print("open menu "))
edit_menu.add_command(label="paste",command=lambda:print("save menu "))


window.mainloop()