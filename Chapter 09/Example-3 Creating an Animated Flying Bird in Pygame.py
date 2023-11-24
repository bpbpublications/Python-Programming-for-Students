# Creating an Animated Flying Bird in Pygame

import pygame as pg
from pygame.locals import *
from sys import exit
pg.init()
screenSurface = pg.display.set_mode((400, 400))
pg.display.set_caption("Flying Bird with arrow keys")
bird_img = pg.image.load('D:/Images/game_image.png').convert_alpha()
flag = False
xloc = 100
yloc= 100
screenSurface.blit(bird_img, (xloc, yloc))
while True:
   screenSurface.fill((255,255,255))
   screenSurface.blit(bird_img, (xloc, yloc))
   for ev in pg.event.get():
      if ev.type == QUIT:
         exit()
      if ev.type == KEYDOWN:
         if ev.key == K_RIGHT:
            xloc= xloc+10
         if ev.key == K_LEFT:
            xloc=xloc-10
         if ev.key == K_UP:
            yloc=yloc-10
         if ev.key == K_DOWN:
            yloc=yloc+10
         pg.display.update()
