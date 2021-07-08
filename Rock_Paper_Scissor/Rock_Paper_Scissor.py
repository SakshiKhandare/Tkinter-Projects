from tkinter import *
import random

#Creating Object
root = Tk()

#Set Geometry
root.geometry("500x350")

#Set Title
root.title("Rock Paper Scissor")

#Computer Value
comp_val = {"0":"Rock","1":"Paper","2":"Scissor"}

#Reset Game
def reset_game():
    b1["state"] = "active"
    b2["state"] = "active"
    b3["state"] = "active"
    l1.config(text="Player           ")
    l3.config(text="Computer")
    l4.config(text="")

#Disable Button
def button_disable():
    b1["state"] = "disable"
    b2["state"] = "disable"
    b3["state"] = "disable"

#When player selects rock
def isrock():
    c_v = comp_val[str(random.randint(0,2))]
    if c_v == "Rock":
        match_res = "Match Draw"
    elif c_v == "Paper":
        match_res = "Computer Win"
    else:
        match_res = "Player Win"

    l1.config(text="Rock           ")
    l3.config(text=c_v)
    l4.config(text=match_res)
    button_disable()


#When player selects paper
def ispaper():
    c_v = comp_val[str(random.randint(0,2))]
    if c_v == "Paper":
        match_res = "Match Draw"
    elif c_v == "Scissor":
        match_res = "Computer Win"
    else:
        match_res = "Player Win"

    l1.config(text="Paper           ")
    l3.config(text=c_v)
    l4.config(text=match_res)
    button_disable()

#When player selects scissor
def isscissor():
    c_v = comp_val[str(random.randint(0,2))]
    if c_v == "Scissor":
        match_res = "Match Draw"
    elif c_v == "Rock":
        match_res = "Computer Win"
    else:
        match_res = "Player Win"

    l1.config(text="Scissor           ")
    l3.config(text=c_v)
    l4.config(text=match_res)
    button_disable()



#Labels Frames Buttons
Label(root,text="Rock Paper Scissor",font="normal 20 bold",fg="blue").pack(pady=20)

frame = Frame(root)
frame.pack()

l1 = Label(frame,text="Player           ",font=10)
l1.pack(side=LEFT)

l2 = Label(frame,text="VS           ",font="normal 15 bold")
l2.pack(side=LEFT)

l3 = Label(frame,text="Computer",font=10)
l3.pack()

l4 = Label(root,text="",font="normal 20 bold",bg="white",width=20,relief="solid")
l4.pack(pady=20)


frame1 = Frame(root)
frame1.pack()

b1 = Button(frame1,text="Rock",font=10,width=7,command=isrock)
b1.pack(side=LEFT,padx=20,pady=10)

b2 = Button(frame1,text="Paper",font=10,width=7,command=ispaper)
b2.pack(side=LEFT,padx=20)

b3 = Button(frame1,text="Scissor",font=10,width=7,command=isscissor)
b3.pack(side=LEFT,padx=20)


Button(root, text = "Reset Game",font = 10, fg = "white",bg = "red", command = reset_game).pack(pady = 20)

root.mainloop()