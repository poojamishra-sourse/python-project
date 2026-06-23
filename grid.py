import tkinter as tk
from tkinter import ttk
window=tk.Tk()
window.title("grid with frame ")
window.geometry("300x200")
#we have created 5 widget 
label1=ttk.Label(window,text="label1",background="red")
label2=ttk.Label(window,text="label2",background="green")
label3=ttk.Label(window,text="label3",background="yellow")
label4=ttk.Label(window,text="label4",background="orange")
label5=ttk.Label(window,text="label5",background="blue")
#creating grid (table structure)
# window.columnconfigure(0,weight=1)
# window.columnconfigure(1,weight=1)
window.columnconfigure((0,1),weight=1)
window.rowconfigure(0,weight=1)
window.rowconfigure(1,weight=1)
window.rowconfigure(2,weight=1)
#place widgets in grid
label1.grid(row=0,column=0,sticky="nsew")
label2.grid(row=0,column=1,sticky="nsew")
label3.grid(row=1,column=0,sticky="nsew")
label4.grid(row=1,column=1,sticky="nsew",rowspan=2)
label5.grid(row=2,column=0,sticky="nsew")#columnspan=2)
window.mainloop()

