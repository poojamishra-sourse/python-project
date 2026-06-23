from tkinter import *
from tkinter import messagebox
import base64
screen=Tk()
screen.geometry("400x400")
screen.title("Encryption and Decryption")
screen.config(bg="black")
def encrypt():
    password=code.get()
    if password=="1234":
            screen1=Toplevel(screen)
            screen1.title("ENCRYPTION")
            screen1.geometry("400x250")
            screen1.config(bg="yellow")
            Message=text1.get(1.0,END)
            encode_message=Message.encode("ascii")
            base64_bytes=base64.b64encode(encode_message)
            encrypt=base64_bytes.decode("ascii")
            Label(screen1,text="ENCRYPTED TEXT",font="arial 10 bold",bg="yellow",fg="black").place(x=10,y=10)
            text2=Text(screen1,font="20",bg="white",fg="black",wrap=WORD)
            text2.place(x=10,y=40,width=380,height=150)
            text2.insert(END,encrypt)
    elif(password==""):
            messagebox.showerror("ERROR"," please enter the secret key")
    elif(password!="1234"):
            messagebox.showerror("ERROR"," please enter the correct secret key")
def decryption():
    password=code.get()
    
    if password=="1234":
                screen2=Toplevel(screen)
                screen2.title("DECRYPTION")
                screen2.geometry("400x250")
                screen2.config(bg="light green")
                Message=text1.get(1.0,END)
                decode_message=Message.encode("ascii")
                base64_bytes=base64.b64decode(decode_message)
                decrypt=base64_bytes.decode("ascii")
                Label(screen2,text="DECRYPTED TEXT",font="arial 10 bold",bg="light green",fg="black").place(x=10,y=10)
                text3=Text(screen2,font="20",bg="white",fg="black",wrap=WORD)
                text3.place(x=10,y=40,width=380,height=150)
                text3.insert(END,decrypt)
    elif(password==""):
                messagebox.showerror("ERROR"," please enter the secret key")
    elif(password!="1234"):
                messagebox.showerror("ERROR"," please enter the correct secret key")                
def reset():
    text1.delete(1.0,END)
    code.set("")
     
#label
Label(screen,text="enter the text for encryption and decryption",font="arial 10 bold",bg="black",fg="white").place(x=50,y=10)
#text visit
text1=Text(screen,font="20")
text1.place(x=5,y=45,width=410,height=120)
#label
Label(screen,text="ENTER SECRET KEY",font="arial 10 bold",bg="white",fg="red").place(x=150,y=180,)
#enter key 
code=StringVar()
Entry(screen,font=" 10 ",bg="white",fg="red",bd=2,show="*",textvariable=code).place(x=140,y=220,width=150)
#button
Button(screen,text="ENCRYPT",font="arial 10 bold",bg="blue",fg="white",command=encrypt).place(x=100,y=280 )
Button(screen,text="DECRYPT",font="arial 10 bold",bg="green",fg="white",command=decryption).place(x=250,y=280)
Button(screen,text="RESET",font="arial 10 bold",bg="red",fg="white",command=reset).place(x=190,y=330)




mainloop()