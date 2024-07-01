from tkinter import * 
from PIL import Image, ImageTk
from random import randint

#background colour
background_color = "#9b59b6"

#main window
root = Tk()
root.title("Rock Paper Scissor")
root.configure(background=background_color)

#indicators
user_indicator_label = Label(root,font=("arial",20,"bold"),text="USER",background=background_color,foreground="white")
user_indicator_label.grid(row=0,column=1,pady=(50, 10))
comp_indicator_label = Label(root,font=("arial",20,"bold"),text="COMPUTER",background=background_color,foreground="white")
comp_indicator_label.grid(row=0,column=3,pady=(50, 10))

#pictures
rock_user_img = ImageTk.PhotoImage(Image.open(r"rock_paper_scissor\images\rock_user.png"))
rock_comp_img = ImageTk.PhotoImage(Image.open(r"rock_paper_scissor\images\rock_comp.png"))
paper_user_img = ImageTk.PhotoImage(Image.open(r"rock_paper_scissor\images\paper_user.png"))
paper_comp_img = ImageTk.PhotoImage(Image.open(r"rock_paper_scissor\images\paper_comp.png"))
scissor_user_img = ImageTk.PhotoImage(Image.open(r"rock_paper_scissor\images\scissor_user.png"))
scissor_comp_img = ImageTk.PhotoImage(Image.open(r"rock_paper_scissor\images\scissor_comp.png"))

#insert picture
user_img_label = Label(root,image = scissor_user_img,font=("arial",20,"bold"),background=background_color)
comp_img_label = Label(root,image = scissor_comp_img,font=("arial",20,"bold"),background=background_color)
user_img_label.grid(row=1,column=0,pady=(90,10),padx=(10,0))
comp_img_label.grid(row=1,column=4,pady=(90,10),padx=(0,10))

#scores
user_score_label = Label(root,text=0,font=("arial",20,"bold"),background=background_color,foreground="white")
comp_score_label = Label(root,text=0,font=("arial",20,"bold"),background=background_color,foreground="white")
user_score_label.grid(row=1,column=1,pady=(50,10))
comp_score_label.grid(row=1,column=3,pady=(50,10))

#buttons
rock_btn = Button(root,width=20,height=2,text="Rock",background="#FF3E4D",font=("arial",20,"bold"),foreground="black",command=lambda:updatde_choice("rock"))
rock_btn.grid(row=2,column=1,pady=(90,10))
paper_btn = Button(root,width=20,height=2,text="Paper",background="#FAD02E",font=("arial",20,"bold"),foreground="black",command=lambda:updatde_choice("paper"))
paper_btn.grid(row=2,column=2,pady=(90,10))
scissor_btn = Button(root,width=20,height=2,text="Scissor",background="#0ABDE3",font=("arial",20,"bold"),foreground="black",command=lambda:updatde_choice("scissor"))
scissor_btn.grid(row=2,column=3,pady=(90,10))

#frame for reset and quit button 
r_q_frame = Frame(root,background=background_color)

#reset button
reset_btn = Button(r_q_frame, text="Reset Game",font=("arial",20,"bold"),command=lambda: reset_game())
reset_btn.pack(side=LEFT,padx=10)

#quit game button
quit_btn = Button(r_q_frame, text="Quit Game",font=("arial",20,"bold"),command=lambda: quit_game())
quit_btn.pack(side=RIGHT,padx=10)

r_q_frame.grid(row=3,rowspan=4,columnspan=5,pady=(90,10))

# end game frame
end_game_frame = Frame(root,background=background_color)
end_game_message = Label(end_game_frame,text="",font=("arial",20,"bold"),background=background_color,foreground="white")
end_game_message.pack(pady=10)
playagain_btn = Button(end_game_frame,text="Play Again",font=("arial",20,"bold"),command=lambda: reset_game())
playagain_btn.pack(pady=10)
end_game_frame.grid(row=1,column=0,rowspan=2,columnspan=5,pady=(0,100))
end_game_frame.grid_remove()  # Hide initially

#update choices
def updatde_choice(user_choice):
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
  
  check_winner()

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
  if(user_score == 5 and comp_score == 5):
    show_endgame_message("It's a Tie!!")
  elif(user_score == 5):
    show_endgame_message("You Win!!")
  elif(comp_score == 5):
    show_endgame_message("Computer Win!!")

def disable_buttons():
  rock_btn.configure(state = DISABLED)
  paper_btn.configure(state = DISABLED)
  scissor_btn.configure(state = DISABLED)
  reset_btn.configure(state = DISABLED)

def active_buttons():
  rock_btn.configure(state = NORMAL)
  paper_btn.configure(state = NORMAL)
  scissor_btn.configure(state = NORMAL)
  reset_btn.configure(state = NORMAL)

def show_endgame_message(message):
    end_game_message.config(text=message)
    end_game_frame.grid()
    disable_buttons()

def reset_game():
    active_buttons()
    user_score_label["text"] = "0"
    comp_score_label["text"] = "0"
    user_img_label.configure(image=scissor_user_img)
    comp_img_label.configure(image=scissor_comp_img)
    end_game_frame.grid_remove()

def quit_game():
  exit()

root.mainloop()