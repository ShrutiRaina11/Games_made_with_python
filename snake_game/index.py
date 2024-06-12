import pygame
from pygame.locals import *
import time

def draw_snake():
  surface.fill((111,123,244))
  surface.blit(snake,(snake_pos_x,snake_pos_y))
  pygame.display.flip()
  
if __name__ == "__main__":
  
  pygame.init() #For initializing pygame

  surface = pygame.display.set_mode((500,500)) #For initilizing the window basic step for pygame program
  surface.fill((111,123,244)) #Fill the background with the colour
  
  snake = pygame.image.load(r"snake_game\resources\block.jpg")
  snake_pos_x = 100
  snake_pos_y = 100
  surface.blit(snake,(snake_pos_x,snake_pos_y)) #for inserting are drawing the things on the window surface blit() is used
  
  pygame.display.flip() #For updating the changes to reflect in the screen (we can use update() also instead of flip())

  running = True
  #Event Loop
  while running:
    for event in pygame.event.get():
      if event.type ==  KEYDOWN:
        if event.key == K_ESCAPE:
          running = False
        elif event.key == K_UP:
          snake_pos_y -= 10
          draw_snake()
        elif event.key == K_DOWN:
          snake_pos_y += 10
          draw_snake()
        elif event.key == K_LEFT:
          snake_pos_x -= 10
          draw_snake()
        elif event.key == K_RIGHT:
          snake_pos_x += 10
          draw_snake()
      elif event.type == QUIT:
        running = False

