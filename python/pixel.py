#https://lorenzod8n.wordpress.com/2007/12/16/pygame-tutorial-5-pixels/
#Baixa som: https://freesound.org/people/Xinematix/sounds/494848/#

import pygame
from pygame.locals import *  #submódulo locals, contêm as variáveis de eventos (mouse, teclado, joystick)
from pygame import mixer

import random
 
# Window dimensions
width = 640
height = 400

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

pygame.init()

pygame.mixer.init()
som = pygame.mixer.Sound("vocal-scape.wav")
som.play(-1)


running = True
while running:
  x = random.randint(0, width-1)
  y = random.randint(0, height-1)
  red = random.randint(0, 255)
  green = random.randint(0, 255)
  blue = random.randint(0, 255)

  screen.set_at((x, y), (red, green, blue))

  for event in pygame.event.get():
     if event.type == pygame.QUIT:
       running = False

  pygame.display.flip() 
  clock.tick(240) 
