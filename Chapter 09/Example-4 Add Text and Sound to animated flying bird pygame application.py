# Let us consider an example to add text and sound to animated flying bird pygame application.

import pygame
from pygame.locals import *
from pygame import mixer

pygame.init()
wt = 900
ht = 500
window = pygame.display.set_mode((wt, ht))
# To display an image
flying_bird_img = pygame.image.load(‘D:/images/bird1.png’)
flying_bird_img = pygame.transform.scale(flying_bird_img, (wt, ht))
# To display and configure text
newfont = pygame.font.SysFont(“Arial”, 50)
newtext = newfont.render(“Welcome to Pygame!!”, True, (255,0,0))
# To add music to pygame application
mixer.init()
mixer.music.load(‘D:/images/HappyMusic.mp3’)
mixer.music.play()
run_flag = True
while run_flag:
    window.blit(flying_bird_img, (0, 0))
    window.blit(newtext, (20, 20))
    for event in pygame.event.get():
        if event.type == QUIT:
            run_flag = False
    pygame.display.update()
pygame.quit()
