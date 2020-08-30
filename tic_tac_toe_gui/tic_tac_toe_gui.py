from tkinter import *
from tkinter import font
import tkinter.messagebox
m = Tk()
m.title("Tic Tac Toe   ")

click = True

#function for checking and initialising
def check(buttons):
    global click
    if(buttons["text"]==" " and click==True):
        buttons["text"] = "X"
        click = False
    elif(buttons["text"]==" " and click==False):
        buttons["text"] = "O"
        click = True

def checker(buttons):
    if(button1["text"]=="X" and button2["text"]=="X" and button3["text"]=="X" or
     button4["text"]=="X" and button5["text"]=="X" and button6["text"]=="X" or
     button7["text"]=="X" and button8["text"]=="X" and button9["text"]=="X" or
     button1["text"]=="X" and button4["text"]=="X" and button7["text"]=="X" or
     button2["text"]=="X" and button5["text"]=="X" and button8["text"]=="X" or
     button3["text"]=="X" and button6["text"]=="X" and button9["text"]=="X" or
     button1["text"]=="X" and button5["text"]=="X" and button9["text"]=="X" or
     button3["text"]=="X" and button5["text"]=="X" and button7["text"]=="X" ):
        tkinter.messagebox.showinfo("Winne X you" , "You won this game")

    elif(button1["text"]=="O" and button2["text"]=="O" and button3["text"]=="O" or
     button4["text"]=="O" and button5["text"]=="O" and button6["text"]=="O" or
     button7["text"]=="O" and button8["text"]=="O" and button9["text"]=="O" or
     button1["text"]=="O" and button4["text"]=="O" and button7["text"]=="O" or
     button2["text"]=="O" and button5["text"]=="O" and button8["text"]=="O" or
     button3["text"]=="O" and button6["text"]=="O" and button9["text"]=="O" or
     button1["text"]=="O" and button5["text"]=="O" and button9["text"]=="O" or
     button3["text"]=="O" and button5["text"]=="O" and button7["text"]=="O" ):
        tkinter.messagebox.showinfo("Winne O you" , "You won this game")


#creating buttons
buttons = StringVar()

button1 = Button(m,text=" " , font=("Times 26 bold"),width=8,height=4, activebackground="saddle brown", bg="old lace", command=lambda:[check(button1),checker(button1)])
button1.grid(row=0,column=0,sticky=S+N+E+W)

button2 = Button(m,text=" " , font=("Helvetica 26 bold"),width=8,height=4, activebackground="saddle brown", bg="old lace", command=lambda:[check(button2),checker(button2)])
button2.grid(row=0,column=1,sticky=S+N+E+W)

button3 = Button(m,text=" " , font=("Helvetica 26 bold"),width=8,height=4, activebackground="saddle brown", bg="old lace", command=lambda:[check(button3),checker(button3)])
button3.grid(row=0,column=2,sticky=S+N+E+W)

button4 = Button(m,text=" " , font=("Helvetica 26 bold"),width=8,height=4, activebackground="saddle brown", bg="old lace", command=lambda:[check(button4),checker(button4)])
button4.grid(row=1,column=0,sticky=S+N+E+W)

button5 = Button(m,text=" " , font=("Helvetica 26 bold"),width=8,height=4, activebackground="saddle brown", bg="old lace", command=lambda:[check(button5),checker(button5)])
button5.grid(row=1,column=1,sticky=S+N+E+W)

button6 = Button(m,text=" " , font=("Helvetica 26 bold"),width=8,height=4, activebackground="saddle brown", bg="old lace", command=lambda:[check(button6),checker(button6)])
button6.grid(row=1,column=2,sticky=S+N+E+W)

button7 = Button(m,text=" " , font=("Helvetica 26 bold"),width=8,height=4, activebackground="saddle brown", bg="old lace", command=lambda:[check(button7),checker(button7)])
button7.grid(row=2,column=0,sticky=S+N+E+W)

button8 = Button(m,text=" " , font=("Helvetica 26 bold"),width=8,height=4, activebackground="saddle brown", bg="old lace", command=lambda:[check(button8),checker(button8)])
button8.grid(row=2,column=1,sticky=S+N+E+W)

button9 = Button(m,text=" " , font=("Helvetica 26 bold"),width=8,height=4, activebackground="saddle brown", bg="old lace", command=lambda:[check(button9),checker(button9)])
button9.grid(row=2,column=2,sticky=S+N+E+W)

m.mainloop()
