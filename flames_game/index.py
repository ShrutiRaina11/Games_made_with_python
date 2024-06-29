from tkinter import *

def remove_matching_letter(person1,person2):  
  for letter in person1:
      for letters in person2:
          if(letter == letters):
              person1 =  person1.replace(letter,"")
              person2 = person2.replace(letters,"")
  return [person1,person2]

def calculate_result(person1,person2,status):
  status.delete(0,END)
  person1 = person1.lower()
  person1 = person1.replace(" ","")
  person2 = person2.lower()
  person2 = person2.replace(" ","")
  ret_list = remove_matching_letter(person1,person2)
  str1 = ret_list[0]
  str2 = ret_list[1]
  count = len(str1) + len(str2)

  result = ["Friends", "Love", "Affection", "Marriage", "Enemy" ,"Siblings"]

  while len(result) > 1:
      split_index = (count%len(result)) - 1
      if (split_index >= 0):
          right = result[split_index+1: ]
          left = result[:split_index]
          result = right + left
      else:
          result = result[:-1]
  
  status.insert(10, result[0])

def reset_game(p1_textbox,p2_textbox,status_textbox):
  p1_textbox.delete(0, END)   
  p2_textbox.delete(0, END) 
  status_textbox.delete(0, END) 

def quit_game():
  exit()

def create_interface():  
  background_colour = "#ADD8E6"  # A soothing pastel teal color
  text_color = "#2F4F4F"  # Dark slate gray for good contrast and readability
  btn_color = "#FFF8DC"  # Cornsilk color for buttons

  root = Tk()
  root.title("Flames Game")
  root.configure(bg=background_colour)
  root.geometry('500x400')
  root.resizable(False, False)

  # Center the window on the screen
  window_width = root.winfo_reqwidth()
  window_height = root.winfo_reqheight()
  position_right = int(root.winfo_screenwidth()/2 - window_width/2)
  position_down = int(root.winfo_screenheight()/2 - window_height/2)
  root.geometry(f"+{position_right}+{position_down}")

  # Person 1 info interface
  p1_frame = Frame(root, bg=background_colour)
  p1_name_label = Label(p1_frame, text="Person 1 Name", bg=background_colour, font=("arial", 20), fg=text_color)
  p1_name_label.pack(side=LEFT, padx=10)
  p1_textbox = Entry(p1_frame, width=30, bd=5)
  p1_textbox.pack(side=RIGHT, padx=10, ipady=3)
  p1_frame.grid(row=0, column=0, pady=(20, 10))

  # Person 2 info interface
  p2_frame = Frame(root, bg=background_colour)
  p2_name_label = Label(p2_frame, text="Person 2 Name", bg=background_colour, font=("arial", 20), fg=text_color)
  p2_name_label.pack(side=LEFT, padx=10)
  p2_textbox = Entry(p2_frame, width=30, bd=5)
  p2_textbox.pack(side=RIGHT, padx=10, ipady=3)
  p2_frame.grid(row=1, column=0, pady=(10, 10))

  # Calculate interface
  calc_frame = Frame(root, bg=background_colour)
  calc_btn = Button(calc_frame, text="Calculate", font=("arial", 12, "bold"), bg=btn_color, command=lambda: calculate_result(p1_textbox.get(), p2_textbox.get(), status_textbox))
  calc_btn.pack(padx=10, pady=5)
  calc_frame.grid(row=2, column=0, pady=(20, 20))

  # Relationship status
  status_frame = Frame(root, bg=background_colour)
  status_label = Label(status_frame, text="Relationship Status", bg=background_colour, font=("arial", 20), fg=text_color)
  status_label.pack(side=LEFT, padx=10)
  status_textbox = Entry(status_frame, width=30, bd=5)
  status_textbox.pack(side=RIGHT, padx=10, ipady=3)
  status_frame.grid(row=3, column=0, pady=(20, 20))

  # Frame for reset and quit button 
  r_q_frame = Frame(root, bg=background_colour)
  # Reset button
  reset_btn = Button(r_q_frame, text="Reset Game", font=("arial", 12, "bold"), bg=btn_color, command=lambda: reset_game(p1_textbox, p2_textbox, status_textbox))
  reset_btn.pack(side=LEFT, padx=10, pady=5)
  # Quit game button
  quit_btn = Button(r_q_frame, text="Quit Game", font=("arial", 12, "bold"), bg=btn_color, command=quit_game)
  quit_btn.pack(side=RIGHT, padx=10, pady=5)
  r_q_frame.grid(row=4, column=0, pady=(20, 10))

  root.mainloop()

if __name__ == "__main__":
  create_interface()