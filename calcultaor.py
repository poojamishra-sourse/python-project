import tkinter as tk
from tkinter import ttk
window=tk.Tk()
window.title("calculator")
window.geometry("400x600")
def button_click(value):
    x=display_var.get()
    display_var.set(x+value)
def calculate():
    # y=eval(display_var.get())  
    # display_var.set(y)
    try:
         y=eval(display_var.get())  
         display_var.set(y)
    except Exception as e:
        display_var.set(e)   
    
    
display_var=tk.StringVar()
display=ttk.Entry(window,textvariable=display_var,font=('arial',20),justify="right")
display.grid(row=0,column=0,columnspan=4,sticky="ewns",padx=5,pady=5)

button_seven=ttk.Button(window,text="7",command=lambda: button_click('7'))
button_seven.grid(row=1,column=0,padx=5,pady=5,sticky="ewns")

button_eight=ttk.Button(window,text="8",command=lambda: button_click('8'))
button_eight.grid(row=1,column=1,padx=5,pady=5,sticky="ewns")

button_nine=ttk.Button(window,text="9",command=lambda: button_click('9'))
button_nine.grid(row=1,column=2,padx=5,pady=5,sticky="ewns")

button_divide=ttk.Button(window,text="/",command=lambda: button_click('/'))
button_divide.grid(row=1,column=3,padx=5,pady=5,sticky="ewns")
#########################################################################3



button_four=ttk.Button(window,text="4",command=lambda: button_click('4'))
button_four.grid(row=2,column=0,padx=5,pady=5,sticky="ewns")

button_five=ttk.Button(window,text="5",command=lambda: button_click('5'))
button_five.grid(row=2,column=1,padx=5,pady=5,sticky="ewns")

button_six=ttk.Button(window,text="6",command=lambda: button_click('6'))
button_six.grid(row=2,column=2,padx=5,pady=5,sticky="ewns")

button_multiply=ttk.Button(window,text="*",command=lambda: button_click('*'))
button_multiply.grid(row=2,column=3,padx=5,pady=5,sticky="ewns")
#################################################################################

button_one=ttk.Button(window,text="1",command=lambda: button_click('1'))
button_one.grid(row=3,column=0,padx=5,pady=5,sticky="ewns")

button_two=ttk.Button(window,text="2",command=lambda: button_click('2'))
button_two.grid(row=3,column=1,padx=5,pady=5,sticky="ewns")

button_three=ttk.Button(window,text="3",command=lambda: button_click('3'))
button_three.grid(row=3,column=2,padx=5,pady=5,sticky="ewns")

button_subtract=ttk.Button(window,text="-",command=lambda: button_click('-'))
button_subtract.grid(row=3,column=3,padx=5,pady=5,sticky="ewns")
########################################################################

button_zero=ttk.Button(window,text="0",command=lambda: button_click('0'))
button_zero.grid(row=4,column=0,padx=5,pady=5,sticky="ewns")

button_dot=ttk.Button(window,text=".",command=lambda: button_click('.'))
button_dot.grid(row=4,column=1,padx=5,pady=5,sticky="ewns")

button_equal_to=ttk.Button(window,text="=",command=calculate)
button_equal_to.grid(row=4,column=2,padx=5,pady=5,sticky="ewns")

button_add=ttk.Button(window,text="+",command=lambda: button_click('+'))
button_add.grid(row=4,column=3,padx=5,pady=5,sticky="ewns")
#############################################################################

button_clear=ttk.Button(window,text="c",command=lambda:display_var.set(""))
button_clear.grid(row=5,columnspan=4,column=0,padx=5,pady=5,sticky="ewns")


for i in range(6):
    window.rowconfigure(i,weight=1)
for j in range(4):
    window.columnconfigure(j,weight=1)  
  

 
window.mainloop()
