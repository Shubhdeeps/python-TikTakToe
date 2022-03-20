from tkinter import *
from tkinter import messagebox

win = Tk()
win.title('Tik Tac Toe game')
win.config(bg="#494949")
clicked = True
count = 0

xwin = 0
ywin = 0



#disable all the buttons
def disablebuttons(winner):      
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)



    
# check winner
def checkwinner():
    global winner
    winner = False

    if b1["text"] == b2["text"] == b3["text"] != " ":
        b1.config(bg="green")
        b2.config(bg="green")
        b3.config(bg="green")
        messagebox.showinfo("Winner", b1["text"] + " wins")
        disablebuttons(b1["text"])

    elif b1["text"] == b4["text"] == b7["text"] != " ":
         b1.config(bg="green")
         b4.config(bg="green")
         b7.config(bg="green")
         messagebox.showinfo("Winner", b1["text"] + " wins")
         disablebuttons(b1["text"])

    elif b4["text"] == b5["text"] == b6["text"] != " ":
        b4.config(bg="green")
        b5.config(bg="green")
        b6.config(bg="green")
        messagebox.showinfo("Winner", b5["text"] + " wins")
        disablebuttons(b1["text"])

    elif b2["text"] == b5["text"] == b8["text"] != " ":
        b2.config(bg="green")
        b5.config(bg="green")
        b8.config(bg="green")
        messagebox.showinfo("Winner", b5["text"] + " wins")
        disablebuttons(b1["text"])

    elif b7["text"] == b8["text"] == b9["text"] != " ":
         b7.config(bg="green")
         b8.config(bg="green")
         b9.config(bg="green")
         messagebox.showinfo("Winner", b9["text"] + " wins")
         disablebuttons(b1["text"])

    elif b3["text"] == b6["text"] == b9["text"] != " ":
         b3.config(bg="green")
         b6.config(bg="green")
         b9.config(bg="green")
         messagebox.showinfo("Winner", b9["text"] + " wins")
         disablebuttons(b1["text"])

    elif b1["text"] == b5["text"] == b9["text"] != " ":
         b1.config(bg="green")
         b5.config(bg="green")
         b9.config(bg="green")
         messagebox.showinfo("Winner", b9["text"] + " wins")
         disablebuttons(b1["text"])

    elif b3["text"] == b5["text"] == b7["text"] != " ":
         b3.config(bg="green")
         b5.config(bg="green")
         b7.config(bg="green")
         messagebox.showinfo("Winner", b3["text"] + " wins")
         disablebuttons(b1["text"])

        
#Button clicked function
def b_click(btn):
    global clicked, count
    if btn["text"] == " " and clicked == True:
        btn["text"] = "X"
        clicked = False
        count += 1
        checkwinner()

    elif btn["text"] == " " and clicked == False:
        btn["text"] = "O"
        clicked = True
        count += 1
        checkwinner()

    else:
        messagebox.showerror("Error", "Already selected")


#to show the current score


#frame to handle buttons
frame = Frame()
frame.pack()

def new_game():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9
    global clicked, count
    global frame
    clicked = True
    count = 0
    
    b1 = Button(frame,text=" ", font=("Helvetics", 20),height=3,width=6,bg="#494949", fg="white", command=lambda: b_click(b1))
    b2 = Button(frame,text=" ",font=("Helvetics", 20),height=3,width=6,bg="#494949", fg="white", command=lambda: b_click(b2))
    b3 = Button(frame,text=" ",font=("Helvetics", 20),height=3,width=6,bg="#494949", fg="white",command=lambda: b_click(b3))

    b4 = Button(frame,text=" ",font=("Helvetics", 20),height=3,width=6,bg="#494949", fg="white",command=lambda: b_click(b4))
    b5 = Button(frame,text=" ",font=("Helvetics", 20),height=3,width=6,bg="#494949", fg="white",command=lambda: b_click(b5))
    b6 = Button(frame,text=" ",font=("Helvetics", 20),height=3,width=6,bg="#494949", fg="white",command=lambda: b_click(b6))

    b7 = Button(frame,text=" ",font=("Helvetics", 20),height=3,width=6,bg="#494949", fg="white",command=lambda: b_click(b7))
    b8 = Button(frame,text=" ",font=("Helvetics", 20),height=3,width=6,bg="#494949", fg="white",command=lambda: b_click(b8))
    b9 = Button(frame,text=" ",font=("Helvetics", 20),height=3,width=6,bg="#494949", fg="white",command=lambda: b_click(b9))

    b1.grid(row=0,column=0)
    b2.grid(row=0,column=1)
    b3.grid(row=0,column=2)

    b4.grid(row=1,column=0)
    b5.grid(row=1,column=1)
    b6.grid(row=1,column=2)

    b7.grid(row=2,column=0)
    b8.grid(row=2,column=1)
    b9.grid(row=2,column=2)

newgame = Button(win, text="New Game", height=2, width=2, padx=70, command=new_game)
newgame.pack(side="left")

quitgame = Button(win, text="Exit Game", height=2, width=2, padx=70, command=win.destroy)
quitgame.pack(side="right")

new_game()

win.mainloop()
