from tkinter import *
from tkinter import messagebox
import base64
import os

def decrypt():
    password = code.get()
    if password == "02010":
        # creating the encryption window
        screen2 = Toplevel(screen)
        screen2.title("Decryption")
        screen2.geometry("400x200")
        screen2.configure(bg="#00bd56")

        # encryption part using b64
        message = text1.get(1.0, END)
        decode_message = message.encode("ascii")
        base64_bytes = base64.b64decode(decode_message)
        decrypt=base64_bytes.decode("ascii")

        Label(screen2, text="DECRYPT", font="arial", fg="white", bg="#00bd56").place(x=10, y=0)
        text2 = Text(screen2, font="Rpbote 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40, width="380", height="150")

        text2.insert(END, decrypt)
    elif password == "":
        messagebox.showerror("encryption", "Secret code?")
    elif password != "02010":
        messagebox.showerror("encryption", "Secret code thappu!")

def encrypt():
    password=code.get()
    if password=="02010":
        #creating the encryption window
        screen1=Toplevel(screen)
        screen1.title("Encryption")
        screen1.geometry("400x200")
        screen1.configure(bg="#ed3833")

        #encryption part using b64
        message=text1.get(1.0,END)
        encode_message=message.encode("ascii")
        base64_bytes=base64.b64encode(encode_message)
        encrypt=base64_bytes.decode("ascii")

        Label(screen1,text="ENCRYPT",font="arial",fg="white",bg="#ed3833").place(x=10,y=0)
        text2=Text(screen1,font="Rpbote 10",bg="white",relief=GROOVE,wrap=WORD,bd=0)
        text2.place(x=10,y=40,width="380",height="150")

        text2.insert(END,encrypt)
    elif password=="":
        messagebox.showerror("encryption","Secret code?")
    elif password!="02010":
        messagebox.showerror("encryption","Secret code thappu!")

def main_screen():
    #declaring variables
    global screen
    global text1
    global code

    #creating the main window
    screen=Tk()
    screen.geometry('375x398')#dimensionsof screen

    screen.title("Gamble-coffer")#title of screen

    def reset():
        code.set("")
        text1.delete(1.0,END)

    #Labeling the input text box
    Label(screen,text="Secret aa sollunga",fg="black",font=("times new roman",13)).place(x=10,y=10)

    #formatting the text box
    text1=Text(screen,font=("Robote 20",13),bg="white",wrap=WORD,bd=0)
    text1.place(x=10,y=40,width=355,height =100)

    #secret code part
    Label(text="Secret Code aa enter pannunga:",fg="black",font=("times new roman",13)).place(x=10,y=160)
    code=StringVar()
    Entry(textvariable=code,width=19,font=("times new roman",25),bd=0,show="*").place(x=10,y=190,width=355)

    #encrypt and decrypt button
    Button(text="ENCRYPT aa?",height="2",width="23",bg="#ed3833",fg="white",bd=0,command=encrypt).place(x=10,y=248)
    Button(text="DECRYPT aa?", height="2", width="23", bg="#00bd56",fg="white",bd=0,command=decrypt).place(x=200, y=248)

    #reset button
    Button(text="RESET pannidlama?",height="2",width="50",bg="#1089ff",fg="white",bd=0,command=reset).place(x=10,y=300)
    screen.mainloop()
main_screen()