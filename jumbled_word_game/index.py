import tkinter as tk
import random
import time

def choose_word():
    word_list=["rainbow","cricket","football","physics","chemistry","condition","players","hidden","chocolate","brownie","flavour","doctor","chief","love","enjoy"]
    word=random.choice(word_list)
    return word

def jumble_word(word):
    word = "".join(random.sample(word,len(word)))
    return word

class JumbledWordGame(tk.Tk):
  def __init__(self):
    super().__init__()

    self.title("Jumbled Word Game")
    self.configure(bg="white")    
    # calling method
    self.UiComponents()

    self.current_word = None
    self.lifeline = 3
    self.score = 0

  def UiComponents(self):
    # Head Label
    head_font = ("Times", 15, "bold", "italic", "underline")
    head_label = tk.Label(self, text="Jumbled Word Game", font=head_font, fg="darkCyan", bg="white")
    head_label.place(x=20, y=10, width=280, height=60)

    # Jumbled Word Label
    self.j_word_label = tk.Label(self, text="", font=("Times", 12), justify='center',  bg="white", relief="solid", bd=2)
    self.j_word_label.place(x=30, y=80, width=260, height=50)

    # Input Entry
    self.input_word_entry = tk.Entry(self, font=("Times", 12), justify='center', bd=2, relief="solid")
    self.input_word_entry.place(x=20, y=150, width=200, height=40)
    self.input_word_entry.focus()  # Focus on input entry initially

    # Check Button
    self.check_button = tk.Button(self, text="Check", font=("Times", 12, "bold"), bg="lightgrey", command=self.check_word)
    self.check_button.place(x=230, y=155, width=80, height=30)

    # Result Label
    self.result_label = tk.Label(self, text="", font=("Times", 13), justify='center', bg="yellow", relief="solid", bd=2)
    self.result_label.place(x=40, y=210, width=240, height=50)

    # Score Label
    self.score_label = tk.Label(self, text="Score: 0", font=("Times", 12, "bold"), bg="white")
    self.score_label.place(x=20, y=280)

    # Lifeline Label
    self.lifeline_label = tk.Label(self, text="❤️❤️❤️", font=("Times", 12, "bold"), bg="white")
    self.lifeline_label.place(x=200, y=280)

    # Start, Skipword and Quit Buttons
    self.start_button = tk.Button(self, text="Start", font=("Times", 12, "bold"), bg="lightgrey", command=self.start_game)
    self.start_button.place(x=15, y=320, width=140, height=40)

    self.skip_word_button = tk.Button(self, text="Skip Word", font=("Times", 12, "bold"), bg="lightgrey", command=self.skip_word)
    self.skip_word_button.place(x=165, y=320, width=140, height=40)
    self.skip_word_button.config(state = tk.DISABLED)

    self.quit_button = tk.Button(self, text="Quit Game", font=("Times", 12, "bold"), bg="lightgrey", command=self.quit_game)
    self.quit_button.place(x=15, y=320, width=140, height=40)
    self.quit_button.place_forget()

  def get_word(self):
    self.current_word = choose_word()
    self.j_word_label.config(text=jumble_word(self.current_word))
    self.input_word_entry.delete(0, tk.END)

  def check_word(self):
    # Implement your check game here
    user_input = self.input_word_entry.get()

    # Example: Check if user input matches the jumbled word
    if user_input == self.current_word:
      self.result_label.config(text="Correct!", bg="lightgreen")
      self.score += 1
      self.score_label.config(text="Score: "+str(self.score))
      time.sleep(0.3)
      self.get_word()
    else:
      self.result_label.config(text="Incorrect!", bg="salmon")
      self.lifeline -= 1
      if(self.lifeline == 2):
        self.lifeline_label.config(text="❤️❤️")
      elif(self.lifeline == 1):
        self.lifeline_label.config(text="❤️")
      elif(self.lifeline == 0):
        self.game_over()

  def start_game(self):
    self.get_word()
    self.quit_button.place(x=15, y=320, width=140, height=40)
    self.skip_word_button.config(state = tk.NORMAL) 

  def skip_word(self):
    # Implement your reset game here
    self.get_word()
    self.result_label.config(text="", bg="yellow")

  def game_over(self):
    self.play_again()

  def play_again(self):
    self.score = 0
    self.score_label.config(text="Score: 0")
    self.lifeline = 3
    self.lifeline_label.config(text="❤️❤️❤️")
    self.j_word_label.config(text="")
    self.input_word_entry.delete(0, tk.END)
    self.result_label.config(text="", bg="yellow")
    self.skip_word_button.config(state = tk.DISABLED)
    self.quit_button.place_forget()

  def quit_game(self):
    exit()

if __name__ == "__main__":
  app = JumbledWordGame()
  app.geometry('350x380')  # Adjusted window size to accommodate new labels and buttons
  app.mainloop()
