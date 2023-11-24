# Let us consider an example to demonstrate different shapes in a Pygame:

import pygame as pg
pg.init()
screenSurface = pg.display.set_mode((700, 700))
done = False
GRAY = (190, 190, 190, 255)
screenSurface.fill(GRAY)
RED = (255, 0, 0)
VIOLET = (238, 130, 238, 255)
GOLD = (255, 215, 0, 255)
CYAN = (0, 255, 255, 255)
ORANGE = (255, 165, 0, 255)
PURPLE = (160, 32, 240, 255)
while not done:
   for event in pg.event.get():
      if event.type == pg.QUIT:
         done = True
   pg.draw.rect(surface=screenSurface, color=VIOLET, rect=(200, 130, 160, 160))
   pg.draw.polygon(surface=screenSurface, color=CYAN, points=((20,380),(80,435),(135,300),(100,325),(220, 380)))
   pg.draw.circle(surface=screenSurface, color=PURPLE, center=(100,100), radius=80)
   pg.draw.line(surface=screenSurface, color=RED, start_pos=(400, 600), end_pos=(550, 500), width=4)
   pg.draw.ellipse(surface=screenSurface, color=GOLD, rect=(400, 200, 300, 70))
   pg.draw.rect(surface=screenSurface, color=ORANGE, rect=(300, 20, 270, 50), width=5)
   pg.draw.circle(surface=screenSurface, color=CYAN, center=(380, 380), radius=60, width=2)
   pg.draw.ellipse(width=5, surface=screenSurface, color=PURPLE, rect=(250, 400, 130, 80))
   pg.display.flip()
