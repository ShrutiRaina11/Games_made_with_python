from tkinter import *
import tkinter.messagebox

root = Tk()
root.title("Tic Tac Toe Multiplayer Game")

player1 = StringVar()
player2 = StringVar()

p1 = StringVar()
p2 = StringVar()

player1_name = Entry(root, textvariable=p1, bd=5)
player1_name.grid(row=1,column=1,columnspan=8)
player2_name = Entry(root, textvariable=p2, bd=5)
player2_name.grid(row=2,column=1,columnspan=8)

bclick = True
flag = 0

def btn_reset():
  button1["text"] = ""
  button2["text"] = ""
  button3["text"] = ""
  button4["text"] = ""
  button5["text"] = ""
  button6["text"] = ""
  button7["text"] = ""
  button8["text"] = ""
  button9["text"] = ""

def disableButton():
  button1.configure(state = DISABLED)
  button2.configure(state = DISABLED)
  button3.configure(state = DISABLED)
  button4.configure(state = DISABLED)
  button5.configure(state = DISABLED)
  button6.configure(state = DISABLED)
  button7.configure(state = DISABLED)
  button8.configure(state = DISABLED)
  button9.configure(state = DISABLED)

def btn_click(button):
  global bclick,flag,player1,player1_name,player2,player2_name
  if button["text"] == " " and bclick == True:
    button["text"] = "X"
    bclick = False
    player1 = p1.get() + " Wins!"
    check_for_win()
    flag += 1
  elif button["text"] == " " and bclick == False:
    button["text"] = "O"
    bclick = True
    player2 = p2.get() + " Wins!"
    check_for_win()
    flag += 1
  else:
    tkinter.messagebox.showinfo("TicTacToe","Button already clicked")

def check_for_win():
  if flag == 8:
    tkinter.messagebox.showinfo("Tic Tac Toe","It's a Tie!!")
    btn_reset()
  elif(button1["text"] == "X" and button2["text"] == "X" and button3["text"] == "X" or 
       button4["text"] == "X" and button5["text"] == "X" and button6["text"] == "X" or 
       button7["text"] == "X" and button8["text"] == "X" and button9["text"] == "X" or 
       button1["text"] == "X" and button5["text"] == "X" and button9["text"] == "X" or 
       button3["text"] == "X" and button5["text"] == "X" and button7["text"] == "X" or 
       button1["text"] == "X" and button4["text"] == "X" and button7["text"] == "X" or 
       button2["text"] == "X" and button5["text"] == "X" and button8["text"] == "X" or 
       button3["text"] == "X" and button6["text"] == "X" and button9["text"] == "X"):
    disableButton()
    tkinter.messagebox.showinfo("Tic Tac Toe",player1)
    btn_reset()
  elif(button1["text"] == "O" and button2["text"] == "O" and button3["text"] == "O" or 
       button4["text"] == "O" and button5["text"] == "O" and button6["text"] == "O" or 
       button7["text"] == "O" and button8["text"] == "O" and button9["text"] == "O" or 
       button1["text"] == "O" and button5["text"] == "O" and button9["text"] == "O" or 
       button3["text"] == "O" and button5["text"] == "O" and button7["text"] == "O" or 
       button1["text"] == "O" and button4["text"] == "O" and button7["text"] == "O" or 
       button2["text"] == "O" and button5["text"] == "O" and button8["text"] == "O" or 
       button3["text"] == "O" and button6["text"] == "O" and button9["text"] == "O"):
    disableButton()
    tkinter.messagebox.showinfo("Tic Tac Toe",player2)
    btn_reset()
  
  
buttons = StringVar()

player1_label = Label(root, text = "Player 1: ", font="Times 20 bold", bg="white", fg="black", height=1,width=8)
player1_label.grid(row=1,column=0)

player2_label = Label(root, text = "Player 2: ", font="Times 20 bold", bg="white", fg="black", height=1,width=8)
player2_label.grid(row=2,column=0)

button1 = Button(root, text=" ", font="Times 20 bold", bg="gray", fg="white", height=4, width=8, command=lambda:btn_click(button1))
button1.grid(row=3, column=0)

button2 = Button(root, text=" ", font="Times 20 bold", bg="gray", fg="white", height=4, width=8, command=lambda:btn_click(button2))
button2.grid(row=3, column=1)

button3 = Button(root, text=" ", font="Times 20 bold", bg="gray", fg="white", height=4, width=8, command=lambda:btn_click(button3))
button3.grid(row=3, column=2)

button4 = Button(root, text=" ", font="Times 20 bold", bg="gray", fg="white", height=4, width=8, command=lambda:btn_click(button4))
button4.grid(row=4, column=0)

button5 = Button(root, text=" ", font="Times 20 bold", bg="gray", fg="white", height=4, width=8, command=lambda:btn_click(button5))
button5.grid(row=4, column=1)

button6 = Button(root, text=" ", font="Times 20 bold", bg="gray", fg="white", height=4, width=8, command=lambda:btn_click(button6))
button6.grid(row=4, column=2)

button7 = Button(root, text=" ", font="Times 20 bold", bg="gray", fg="white", height=4, width=8, command=lambda:btn_click(button7))
button7.grid(row=5, column=0)

button8 = Button(root, text=" ", font="Times 20 bold", bg="gray", fg="white", height=4, width=8, command=lambda:btn_click(button8))
button8.grid(row=5, column=1)

button9 = Button(root, text=" ", font="Times 20 bold", bg="gray", fg="white", height=4, width=8, command=lambda:btn_click(button9))
button9.grid(row=5, column=2)

root.mainloop()