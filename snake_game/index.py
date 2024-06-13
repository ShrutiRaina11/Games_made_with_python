import pygame
from pygame.locals import *
import time
from random import randint

size = 40 #it same as the dimension of my snake image asa my snke image is 40*40

class Apple:
  def __init__(self,parent_screen):
    self.apple = pygame.image.load(r"snake_game\resources\apple.jpg")
    self.apple_pos_x = size*3
    self.apple_pos_y = size*3
    self.parent_screen = parent_screen

  def draw_apple(self):
    #self.parent_screen.fill((111,123,244))
    self.parent_screen.blit(self.apple,(self.apple_pos_x,self.apple_pos_y)) #For inserting are drawing the things on the window surface blit() is used
    pygame.display.flip()

  def move_apple(self):
    self.apple_pos_x = randint(1,8)*size
    self.apple_pos_y = randint(1,8)*size
    #self.draw_apple()

class Snake:
  def __init__(self,parent_screen,length):
    self.snake = pygame.image.load(r"snake_game\resources\snake.jpg")
    self.snake_length = length
    self.snake_pos_x = [size]*self.snake_length
    self.snake_pos_y = [size]*self.snake_length
    self.parent_screen = parent_screen
    self.direction = None

  def draw_snake(self):
    self.parent_screen.fill((111,123,244))
    for i in range(self.snake_length):
      self.parent_screen.blit(self.snake,(self.snake_pos_x[i],self.snake_pos_y[i])) #For inserting are drawing the things on the window surface blit() is used
    pygame.display.flip() #For updating the changes to reflect in the screen (we can use update() also instead of flip())
  
  def increase_snake_length(self):
    self.snake_length += 1
    self.snake_pos_x.append(-1)
    self.snake_pos_y.append(-1)
 
  def move_up(self):
    self.direction = "up"
     
  def move_down(self):
    self.direction = "down"

  def move_left(self):
    self.direction = "left"

  def move_right(self):
    self.direction = "right"

  def snake_walk(self):
    for i in range(self.snake_length-1,0,-1):
      self.snake_pos_x[i] = self.snake_pos_x[i-1]
      self.snake_pos_y[i] = self.snake_pos_y[i-1]

    if self.direction == "up":
       self.snake_pos_y[0] -= size
    elif self.direction == "down":
       self.snake_pos_y[0] += size
    elif self.direction == "left":
       self.snake_pos_x[0] -= size
    elif self.direction == "right":
       self.snake_pos_x[0] += size
    self.draw_snake()

class Game:
  def __init__(self):
    pygame.init() #For initializing pygame
    self.surface = pygame.display.set_mode((400,400)) #For initilizing the window basic step for pygame program
    self.surface.fill((111,123,244)) #Fill the background with the colour
    self.snake = Snake(self.surface,3)
    self.snake.draw_snake()
    self.apple = Apple(self.surface)
    self.apple.draw_apple()

  def is_collision(self,pos_x1,pos_y1,pos_x2,pos_y2):
    if pos_x1 >= pos_x2 and pos_x1 < pos_x2 + size:
      if pos_y1 >= pos_y2 and pos_y1 < pos_y2 + size:
        return True
    return False
  
  def play(self):
    self.snake.snake_walk()
    self.apple.draw_apple()

    if self.is_collision(self.snake.snake_pos_x[0],self.snake.snake_pos_y[0],self.apple.apple_pos_x,self.apple.apple_pos_y):
      self.apple.move_apple()
      self.snake.increase_snake_length()

  def run(self):
    running = True
    #Event Loop
    while running:
      for event in pygame.event.get():
        if event.type ==  KEYDOWN:
          if event.key == K_ESCAPE:
            running = False
          elif event.key == K_UP:
            self.snake.move_up()
          elif event.key == K_DOWN:
            self.snake.move_down()
          elif event.key == K_LEFT:
            self.snake.move_left()
          elif event.key == K_RIGHT:
            self.snake.move_right()
        elif event.type == QUIT:
          running = False

      self.play()
      time.sleep(0.2)
  
if __name__ == "__main__":
  game = Game()
  game.run()