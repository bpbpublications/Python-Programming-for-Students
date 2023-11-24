# Create a bouncing ball using sprites in Pygame.

import pygame
from sys import exit
screen_width = 1480
screen_height = 820
pygame.init()
clock = pygame.time.Clock()
class FootBall(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y) -> None:
        super().__init__()
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.speed = [5, 5]
        self.image = pygame.image.load('D:\images\FootBall.png')
        self.rect = self.image.get_rect(center=(self.pos_x, self.pos_y))
    def update(self):
        self.detect_collision()
        # To update horizontal position of football
        self.rect.x += self.speed[0]
        # To update vertical position of the football
        self.rect.y += self.speed[1]  

    def detect_collision(self):
        # To detect collision with screen walls and change direction
        if self.rect.right >= screen_width:
            self.speed[0] *= -1
        elif self.rect.left <= 0:
            self.speed[0] *= -1
        if self.rect.top <= 0:
            self.speed[1] *= -1
        elif self.rect.bottom >= screen_height:
            self.speed[1] *= -1
# To Setup display screen
game_window = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Sprites and Collision')                 # To create display caption
football_sprite = FootBall(screen_width / 2, screen_height / 2)     # To create football class instance
football_group = pygame.sprite.Group()                              # To create a football sprite group
football_group.add(football_sprite)                                 # To add a football sprite to the sprite group
# Design a game loop
while True:
    game_window.fill((0, 125, 125))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    football_group.update()  # Call update() to update the sprites
    football_group.draw(game_window)  # To draw all sprites in group
    pygame.display.update()
    clock.tick(50)
