import pygame
from pygame.locals import *
import time

class Snake:
  def __init__(self,parent_screen):
    self.snake = pygame.image.load(r"snake_game\resources\block.jpg")
    self.snake_pos_x = 100
    self.snake_pos_y = 100
    self.parent_screen = parent_screen
    self.direction = None

  def draw_snake(self):
    self.parent_screen.fill((111,123,244))
    self.parent_screen.blit(self.snake,(self.snake_pos_x,self.snake_pos_y)) #For inserting are drawing the things on the window surface blit() is used
    pygame.display.flip() #For updating the changes to reflect in the screen (we can use update() also instead of flip())
  
  def move_up(self):
    self.direction = "up"
     
  def move_down(self):
    self.direction = "down"

  def move_left(self):
    self.direction = "left"

  def move_right(self):
    self.direction = "right"

  def snake_walk(self):
    if self.direction == "up":
       self.snake_pos_y -= 10
    elif self.direction == "down":
       self.snake_pos_y += 10
    elif self.direction == "left":
       self.snake_pos_x -= 10
    elif self.direction == "right":
       self.snake_pos_x += 10
    self.draw_snake()

class Game:
  def __init__(self):
    pygame.init() #For initializing pygame
    self.surface = pygame.display.set_mode((500,500)) #For initilizing the window basic step for pygame program
    self.surface.fill((111,123,244)) #Fill the background with the colour
    self.snake = Snake(self.surface)
    self.snake.draw_snake()

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
      self.snake.snake_walk()
      time.sleep(0.2)
  
if __name__ == "__main__":
  game = Game()
  game.run()