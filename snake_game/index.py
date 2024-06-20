import pygame
from pygame.locals import *
import time
from random import randint

size = 40 #it same as the dimension of my snake image i.e 40*40
screen_width = 1200
screen_height = 800

fps = pygame.time.Clock() # FPS (frames per second) controller

class Apple:
  def __init__(self,parent_screen):
    self.apple = pygame.image.load(r"snake_game\resources\apple.jpg")
    self.apple_pos_x = size*3
    self.apple_pos_y = size*8
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
    self.snake_speed = 8

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

  def reset(self):
    del self.snake
    del self.apple
    self.snake = Snake(self.screen,1)
    self.apple = Apple(self.screen)

  def render_background(self):
    bg = pygame.image.load(r"snake_game\resources\background.jpg")
    self.screen.blit(bg, (0,0))

  def is_apple_eaten(self,pos_x1,pos_y1,pos_x2,pos_y2):
    if pos_x1 == pos_x2 and pos_y1 == pos_y2 :
      return True
    return False
  
  def is_snake_collision_with_itself(self):
    for i in range(3, self.snake.snake_length):
      if self.snake.snake_pos_x[0] == self.snake.snake_pos_x[i] and self.snake.snake_pos_y[0] == self.snake.snake_pos_y[i]:
        return True
    return False
  
  def is_snake_collision_with_wall(self):
    if self.snake.snake_pos_x[0] >= screen_width:
      self.snake.snake_pos_x[0] = 0
      return True
    elif self.snake.snake_pos_x[0] < 0:
      self.snake.snake_pos_x[0] = screen_width - size
      return True
    elif self.snake.snake_pos_y[0] >= screen_height:
      self.snake.snake_pos_y[0] = 0
      return True
    elif self.snake.snake_pos_y[0] < 0:
      self.snake.snake_pos_y[0] = screen_height - size
      return True
    return False
  
  def display_score(self):
    font = pygame.font.SysFont('arial',30)
    score = font.render(f"Score: {self.snake.snake_length}",True,(200,200,200))
    score_rect = score.get_rect()
    self.screen.blit(score,score_rect)

  def show_game_over(self):
      self.render_background()
      font = pygame.font.SysFont('arial', 30)
      line1 = font.render(f"Game is over! Your score is {self.snake.snake_length}", True, (255, 255, 255))
      line1_rect = line1.get_rect(center=((screen_width/2),(screen_height/2)))
      self.screen.blit(line1,line1_rect)
      line2 = font.render("To play again press Enter. To exit press Escape!", True, (255, 255, 255))
      line2_rect = line1.get_rect(center=((screen_width/2)-100,(screen_height/2)+100))
      self.screen.blit(line2,line2_rect)
      pygame.display.flip()

  def play(self):
    self.render_background()
    self.snake.snake_walk()
    self.apple.draw_apple()
    self.display_score()

    if self.is_apple_eaten(self.snake.snake_pos_x[0],self.snake.snake_pos_y[0],self.apple.apple_pos_x,self.apple.apple_pos_y):
      self.apple.move_apple()
      self.snake.increase_snake_length()

    if self.is_snake_collision_with_wall():
      raise "Collision Occured"

    if(self.snake.snake_length >= 4):
      if self.is_snake_collision_with_itself():
        raise "Collision Occured"

    pygame.display.flip() #For updating the changes to reflect in the screen (we can use update() also instead of flip())
    fps.tick(self.snake.snake_speed)

  def run(self):
    running = True
    #Event Loop
    while True:
      for event in pygame.event.get():
        if event.type ==  KEYDOWN:
          if event.key == K_ESCAPE:          
            pygame.quit() # deactivating pygame library                        
            quit() # quit the program
          elif event.key  == K_RETURN: # for enter key
            self.reset()
            running = True
          elif event.key == K_UP:
            self.snake.move_up()
          elif event.key == K_DOWN:
            self.snake.move_down()
          elif event.key == K_LEFT:
            self.snake.move_left()
          elif event.key == K_RIGHT:
            self.snake.move_right()
        elif event.type == QUIT:
          pygame.quit() # deactivating pygame library                        
          quit() # quit the program
      try:
        if running:
            self.play()
      except Exception as e:
        self.show_game_over()
        running = False

if __name__ == "__main__":
  game = Game()
  game.run()