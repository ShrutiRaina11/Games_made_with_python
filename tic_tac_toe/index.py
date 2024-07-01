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
  global bclick,flag
  buttons[0]["text"] = ""
  buttons[1]["text"] = ""
  buttons[2]["text"] = ""
  buttons[3]["text"] = ""
  buttons[4]["text"] = ""
  buttons[5]["text"] = ""
  buttons[6]["text"] = ""
  buttons[7]["text"] = ""
  buttons[8]["text"] = ""
  bclick = True
  flag = 0

def activeButton():
  buttons[0].configure(state = NORMAL)
  buttons[1].configure(state = NORMAL)
  buttons[2].configure(state = NORMAL)
  buttons[3].configure(state = NORMAL)
  buttons[4].configure(state = NORMAL)
  buttons[5].configure(state = NORMAL)
  buttons[6].configure(state = NORMAL)
  buttons[7].configure(state = NORMAL)
  buttons[8].configure(state = NORMAL)

def disableButton():
  buttons[0].configure(state = DISABLED)
  buttons[1].configure(state = DISABLED)
  buttons[2].configure(state = DISABLED)
  buttons[3].configure(state = DISABLED)
  buttons[4].configure(state = DISABLED)
  buttons[5].configure(state = DISABLED)
  buttons[6].configure(state = DISABLED)
  buttons[7].configure(state = DISABLED)
  buttons[8].configure(state = DISABLED)

def btn_click(button):
  global bclick,flag,player1,player1_name,player2,player2_name
  if button["text"] == "" and bclick == True:
    button["text"] = "X"
    bclick = False
    player1 = p1.get() + " Wins!"
    flag += 1
    check_for_win()
  elif button["text"] == "" and bclick == False:
    button["text"] = "O"
    bclick = True
    player2 = p2.get() + " Wins!"
    flag += 1
    check_for_win()
  else:
    tkinter.messagebox.showinfo("TicTacToe","Button already clicked")

def check_for_win():
  if(buttons[0]["text"] == "X" and buttons[1]["text"] == "X" and buttons[2]["text"] == "X" or 
       buttons[3]["text"] == "X" and buttons[4]["text"] == "X" and buttons[5]["text"] == "X" or 
       buttons[6]["text"] == "X" and buttons[7]["text"] == "X" and buttons[8]["text"] == "X" or 
       buttons[0]["text"] == "X" and buttons[4]["text"] == "X" and buttons[8]["text"] == "X" or 
       buttons[2]["text"] == "X" and buttons[4]["text"] == "X" and buttons[6]["text"] == "X" or 
       buttons[0]["text"] == "X" and buttons[3]["text"] == "X" and buttons[6]["text"] == "X" or 
       buttons[1]["text"] == "X" and buttons[4]["text"] == "X" and buttons[7]["text"] == "X" or 
       buttons[2]["text"] == "X" and buttons[5]["text"] == "X" and buttons[8]["text"] == "X"):
    winner("Tic Tac Toe",player1)

  elif flag == 9:
    winner("Tic Tac Toe","It's a Tie!!")

  elif(buttons[0]["text"] == "O" and buttons[1]["text"] == "O" and buttons[2]["text"] == "O" or 
       buttons[3]["text"] == "O" and buttons[4]["text"] == "O" and buttons[5]["text"] == "O" or 
       buttons[6]["text"] == "O" and buttons[7]["text"] == "O" and buttons[8]["text"] == "O" or 
       buttons[0]["text"] == "O" and buttons[4]["text"] == "O" and buttons[8]["text"] == "O" or 
       buttons[2]["text"] == "O" and buttons[4]["text"] == "O" and buttons[6]["text"] == "O" or 
       buttons[0]["text"] == "O" and buttons[3]["text"] == "O" and buttons[6]["text"] == "O" or 
       buttons[1]["text"] == "O" and buttons[4]["text"] == "O" and buttons[7]["text"] == "O" or 
       buttons[2]["text"] == "O" and buttons[5]["text"] == "O" and buttons[8]["text"] == "O"):
    winner("Tic Tac Toe",player2)

def winner(msg,player):
  disableButton()
  tkinter.messagebox.showinfo(msg,player)
  btn_reset()
  activeButton()

player1_label = Label(root, text = "Player 1: ", font="Times 20 bold", bg="white", fg="black", height=1,width=8)
player1_label.grid(row=1,column=0)

player2_label = Label(root, text = "Player 2: ", font="Times 20 bold", bg="white", fg="black", height=1,width=8)
player2_label.grid(row=2,column=0)

buttons = []

for i in range(3, 6):
    for j in range(3):
        button = Button(root, text="", font="Times 20 bold", bg="gray", fg="white", height=4, width=8)
        button.config(command=lambda btn=button: btn_click(btn))
        button.grid(row=i, column=j)
        buttons.append(button)

root.mainloop()