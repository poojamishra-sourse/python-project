import tkinter as tk 
from tkinter import ttk
window =tk.Tk()
window.title("pack with frame ")
window.geometry("400x300")
#frame 1
frame1=tk.Frame(master=window,)
label_1=ttk.Label(master=frame1,text="label1",background="red")
label_2=ttk.Label(master=frame1,text="label_2",background="green")
label_1.pack(side="left", fill="both",expand=True)
label_2.pack(side="left", fill="both",expand=True)

#widget
label_3=ttk.Label(master=window,text="label3",background="yellow")
#frame2
frame2=ttk.Frame(master=window)
frame2_1=ttk.Frame(master=frame2)
frame2_2=ttk.Frame(master=frame2)


b1=ttk.Button(master=frame2_1,text="button1", )
b2=ttk.Button(master=frame2_1,text="button2",)
b3=ttk.Button(master=frame2_1,text="button3",)

b1.pack(fill="both", expand=True)
b2.pack(fill="both", expand=True)
b3.pack(fill="both", expand=True)
frame2_1.pack(side="left", expand=True, fill="both")

Label_4=ttk.Label(master=frame2_2,text="label4",background="orange")
Label_4.pack(expand=True,fill="both")
frame2_2.pack(side="left", expand=True)



#layout  
frame1.pack(expand=True,fill="both")
label_3.pack(expand=True,fill="both")
frame2.pack(expand=True,fill="both")
#frame2_2.pack(side="left")













window.mainloop()

