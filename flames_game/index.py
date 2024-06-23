from tkinter import *

def remove_matching_letter(person1,person2):  
  for letter in person1:
      for letters in person2:
          if(letter == letters):
              person1 =  person1.replace(letter,"")
              person2 = person2.replace(letters,"")
  return [person1,person2]

def calculate_result(person1,person2):
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

def create_interface():  
  background_colour = "#9b59b6"
  root = Tk()
  root.title("Flames Game")
  root.configure(bg=background_colour)

  #person1 info interface
  p1_frame = Frame(root,bg=background_colour)
  p1_name_label = Label(p1_frame,text="Person 1 Name",bg=background_colour,font=("arial",20),fg="white")
  p1_name_label.pack(side=LEFT,padx=10)
  p1_textbox = Entry(p1_frame,width=50,bd=5)
  p1_textbox.pack(side=RIGHT,padx=10,ipady=3)
  p1_frame.grid(row=0,column=0,pady=(10,10))

  #person2 info interface
  p2_frame = Frame(root,bg=background_colour)
  p2_name_label = Label(p2_frame,text="Person 2 Name",bg=background_colour,font=("arial",20),fg="white")
  p2_name_label.pack(side=LEFT,padx=10)
  p2_textbox = Entry(p2_frame,width=50,bd=5)
  p2_textbox.pack(side=RIGHT,padx=10,ipady=3)
  p2_frame.grid(row=1,column=0,pady=(10,10))

  root.mainloop()

if __name__ == "__main__":
  create_interface()