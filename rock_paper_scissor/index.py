from tkinter import *
from PIL import Image, ImageTk
from random import randint

#main window
root = Tk()
root.title("Rock Paper Scissor")
root.configure(background="#9b59b6")


check_for_winner = 0

#indicators
user_indicator_label = Label(root,font=50,text="USER",background="#9b59b6",foreground="white")
user_indicator_label.grid(row=0,column=1)
comp_indicator_label = Label(root,font=50,text="COMPUTER",background="#9b59b6",foreground="white")
comp_indicator_label.grid(row=0,column=3)

#pictures
rock_user_img = ImageTk.PhotoImage(Image.open(r"rock_paper_scissor\images\rock_user.png"))
rock_comp_img = ImageTk.PhotoImage(Image.open(r"rock_paper_scissor\images\rock_comp.png"))
paper_user_img = ImageTk.PhotoImage(Image.open(r"rock_paper_scissor\images\paper_user.png"))
paper_comp_img = ImageTk.PhotoImage(Image.open(r"rock_paper_scissor\images\paper_comp.png"))
scissor_user_img = ImageTk.PhotoImage(Image.open(r"rock_paper_scissor\images\scissor_user.png"))
scissor_comp_img = ImageTk.PhotoImage(Image.open(r"rock_paper_scissor\images\scissor_comp.png"))

#insert picture
user_img_label = Label(root,image = scissor_user_img,background="#9b59b6")
comp_img_label = Label(root,image = scissor_comp_img, background="#9b59b6")
user_img_label.grid(row=1,column=0)
comp_img_label.grid(row=1,column=4)

#scores
user_score_label = Label(root,text=0,font=100,background="#9b59b6",foreground="white")
comp_score_label = Label(root,text=0,font=100,background="#9b59b6",foreground="white")
user_score_label.grid(row=1,column=1)
comp_score_label.grid(row=1,column=3)

#buttons
rock_btn = Button(root,width=20,height=2,text="Rock",background="#FF3E4D",foreground="white",command=lambda:updatde_choice("rock"))
rock_btn.grid(row=2,column=1)
paper_btn = Button(root,width=20,height=2,text="Paper",background="#FAD02E",foreground="white",command=lambda:updatde_choice("paper"))
paper_btn.grid(row=2,column=2)
scissor_btn = Button(root,width=20,height=2,text="Scissor",background="#0ABDE3",foreground="white",command=lambda:updatde_choice("scissor"))
scissor_btn.grid(row=2,column=3)

#message
msg_label = Label(root,text="",font=50,background="#9b59b6",foreground="white")
msg_label.grid(row=3,column=2)

#update choices
def updatde_choice(user_choice):
  global check_for_winner
  #for user
  if user_choice=="rock":
    user_img_label.configure(image=rock_user_img)
  elif user_choice=="paper":
    user_img_label.configure(image=paper_user_img)
  elif user_choice=="scissor":
    user_img_label.configure(image=scissor_user_img)

  #for computer
  choices = ["rock","paper","scissor"]
  comp_choice = choices[randint(0,2)]
  if comp_choice=="rock":
    comp_img_label.configure(image=rock_comp_img)
  elif comp_choice=="paper":
    comp_img_label.configure(image=paper_comp_img)
  elif comp_choice=="scissor":
    comp_img_label.configure(image=scissor_comp_img)

  update_score(user_choice,comp_choice)
  
  check_for_winner += 1
  if(check_for_winner == 10):
    check_winner()
  
#update message
def update_message(message):
  msg_label["text"] = message

#update user score
def update_user_score():
  score = int(user_score_label["text"])
  score += 1
  user_score_label["text"] = str(score)

#update computer score
def update_comp_score():
  score = int(comp_score_label["text"])
  score += 1
  comp_score_label["text"] = str(score)

#check winner
def update_score(user_choice,comp_choice):
  if user_choice == "rock":
    if comp_choice == "paper":
      update_comp_score()
    elif comp_choice == "scissor":
      update_user_score()
  elif user_choice == "paper":
    if comp_choice == "rock":
      update_user_score()
    elif comp_choice == "scissor":
      update_comp_score()
  elif user_choice == "scissor":
    if comp_choice == "rock":
      update_comp_score()
    elif comp_choice == "paper":
      update_user_score()
  else:
    pass

def check_winner():
  user_score = int(user_score_label["text"])
  comp_score = int(comp_score_label["text"])
  if(user_score == comp_score):
    update_message("It's a Tie!!")
  elif(user_score >= comp_score):
    update_message("You Win!!")
  elif(user_score <= comp_score):
    update_message("Computer Win!!")
 
root.mainloop()