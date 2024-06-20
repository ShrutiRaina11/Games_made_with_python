import pygame
from pygame.locals import *
import time
from random import randint

size = 40 #it same as the dimension of my snake image asa my snke image is 40*40
screen_width = 1200
screen_height = 800
background_colour = 111,123,244

fps = pygame.time.Clock() # FPS (frames per second) controller

class Apple:
  def __init__(self,parent_screen):
    self.apple = pygame.image.load(r"snake_game\resources\apple.jpg")
    self.apple_pos_x = size*3
    self.apple_pos_y = size*3
    self.parent_screen = parent_screen

  def draw_apple(self):
    self.parent_screen.blit(self.apple,(self.apple_pos_x,self.apple_pos_y)) #For inserting are drawing the things on the window screen blit() is used

  def move_apple(self):
    self.apple_pos_x = randint(1,(screen_width/size)-1)*size
    self.apple_pos_y = randint(1,(screen_height/size)-1)*size

class Snake:
  def __init__(self,parent_screen,length):
    self.snake = pygame.image.load(r"snake_game\resources\snake.jpg")
    self.snake_length = length
    self.snake_pos_x = [size]*self.snake_length
    self.snake_pos_y = [size]*self.snake_length
    self.parent_screen = parent_screen
    self.direction = None
    self.snake_speed = 6

  def draw_snake(self):
    for i in range(self.snake_length):
      self.parent_screen.blit(self.snake,(self.snake_pos_x[i],self.snake_pos_y[i])) #For inserting are drawing the things on the window screen blit() is used

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
    self.screen = pygame.display.set_mode((screen_width,screen_height)) #For initilizing the window basic step for pygame program
    self.snake = Snake(self.screen,1)
    self.apple = Apple(self.screen)

  def render_background(self):
    bg = pygame.image.load(r"snake_game\resources\background.jpg")
    self.screen.blit(bg, (0,0))

  def snake_collision_with_wall(self,snake_pos_x, snake_pos_y):
    if(snake_pos_x >= (screen_width-size)  or snake_pos_x <= 0):
      self.snake.move_down()
    if(snake_pos_y >= (screen_height-size) or snake_pos_y <= 0):
      self.snake.move_right()

  def is_apple_eaten(self,pos_x1,pos_y1,pos_x2,pos_y2):
    if pos_x1 == pos_x2 and pos_y1 == pos_y2 :
      return True
    return False
  
  def display_score(self):
    font = pygame.font.SysFont('arial',30)
    score = font.render(f"Score: {self.snake.snake_length}",True,(200,200,200))
    score_rect = score.get_rect()
    self.screen.blit(score,score_rect)

  def play(self):
    self.render_background()
    self.snake.snake_walk()
    self.apple.draw_apple()
    self.display_score()

    if self.is_apple_eaten(self.snake.snake_pos_x[0],self.snake.snake_pos_y[0],self.apple.apple_pos_x,self.apple.apple_pos_y):
      self.apple.move_apple()
      self.snake.increase_snake_length()
    
    self.snake_collision_with_wall(self.snake.snake_pos_x[0],self.snake.snake_pos_y[0])

    pygame.display.flip() #For updating the changes to reflect in the screen (we can use update() also instead of flip())
    fps.tick(self.snake.snake_speed)

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

if __name__ == "__main__":
  game = Game()
  game.run()