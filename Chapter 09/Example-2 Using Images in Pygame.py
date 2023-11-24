# Let us see a demonstration of using images in Pygame:

import pygame as pg
pg.init()
screenSurface = pg.display.set_mode((400, 400))
bird_img = pg.image.load('D:/Images/game_image.png').convert_alpha()
flag = False
bgColor = (255,255,255)
while not flag:
   for ev in pg.event.get():
      screenSurface.fill(bgColor)
      rect = bird_img.get_rect()
      rect.center = 100, 100
      screenSurface.blit(bird_img, rect)
      if ev.type == pg.QUIT:
         flag = True
   pg.display.update()
