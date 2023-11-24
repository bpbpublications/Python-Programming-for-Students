# Sample project with solution
# Create a Snake-catching prey game using Pygame and display the total score based on the maximum prey caught. 
# The player’s main goal in this game is to catch as much prey as possible without colliding with the wall. 
# Snake body increases in length with the increasing number of preys caught. 
# We make sure that the snake will always travel to the right of the screen whenever the game starts. 
# Once the snake collides with the screen walls or touches itself, the game ends by displaying the final score:

# Solution

# importing libraries

import pygame as pg
import time
import random
snake_moving_speed = 10
# Set Screen size
screen_x = 800
screen_y = 500
# To define color constants
Black = pg.Color(0, 0, 0)
Green = pg.Color(0, 255, 0)
White = pg.Color(255, 255, 255)
Blue = pg.Color(0, 0, 255)
Red = pg.Color(255, 0, 0)
# Initialising pygame using init()
pg.init()
# To configure screen window
pg.display.set_caption('Snake Catching Prey')
screen_game = pg.display.set_mode((screen_x, screen_y))
# Controlling FPS (frames per second) to display
frames_ps = pg.time.Clock()
# The initial location of snake
snake_location = [100, 100]
# Represent 3 blocks comprising snake body
body_snake = [[100, 100],[90, 100],[80, 100]]
# To define prey location
prey_location = [random.randrange(1, (screen_x // 10)) * 10, random.randrange(1, (screen_y // 10)) * 10]
prey_spawn = True
# Assign default direction for snake movement towards right
default_dir = 'RIGHT'
update_to = default_dir
# Define initial score for user
init_score = 0
# To define update Score function
def update_score(ch, color, font, size):
    # Define font object to display score
    font_obj = pg.font.SysFont(font, size)
    # Now create the display surface object
    score_surface_obj = font_obj.render('Score : ' + str(init_score), True, color)
    # To define a rectangular object for the text surface object
    score_rect_obj = score_surface_obj.get_rect()
    # To display user score
    screen_game.blit(score_surface_obj, score_rect_obj)
# Define function to over the game
def game_over():
    # creating font object my_font
    new_font = pg.font.SysFont('Arial', 30)
    # To define a text surface to draw score text
    game_end_surface = new_font.render('Final Score: ' + str(init_score), True, Green)
    # To create a rectangular object for the text surface object
    game_end_rect = game_end_surface.get_rect()
    # To define position of the text display
    game_end_rect.midtop = (screen_x / 2, screen_y / 4)
    screen_game.blit(game_end_surface, game_end_rect)
    pg.display.flip()
    # To quit the program after 5 seconds
    time.sleep(5)
    pg.quit()
    quit()
# Define event loop
while True:
    # To manage key events
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
                update_to = 'UP'
            if event.key == pg.K_DOWN:
                update_to = 'DOWN'
            if event.key == pg.K_LEFT:
                update_to = 'LEFT'
            if event.key == pg.K_RIGHT:
                update_to = 'RIGHT'
    # No movement if two keys pressed simultaneously
    if update_to == 'UP' and default_dir != 'DOWN':
        default_dir = 'UP'
    if update_to == 'DOWN' and default_dir != 'UP':
        default_dir = 'DOWN'
    if update_to == 'LEFT' and default_dir != 'RIGHT':
        default_dir = 'LEFT'
    if update_to == 'RIGHT' and default_dir != 'LEFT':
        default_dir = 'RIGHT'
    # Define movement of the snake in directions
    if default_dir == 'UP':
        snake_location[1] -= 10
    if default_dir == 'DOWN':
        snake_location[1] += 10
    if default_dir == 'LEFT':
        snake_location[0] -= 10
    if default_dir == 'RIGHT':
        snake_location[0] += 10
    # Snake body increasing on catching prey then scores increased by 10
    body_snake.insert(0, list(snake_location))
    if snake_location[0] == prey_location[0] and snake_location[1] == prey_location[1]:
        init_score += 10
        prey_spawn = False
    else:
        body_snake.pop()
    if not prey_spawn:
        prey_location = [random.randrange(1, (screen_x // 10)) * 10,
                          random.randrange(1, (screen_y // 10)) * 10]
    prey_spawn = True
    screen_game.fill(White)
    for pos in body_snake:
        pg.draw.rect(screen_game, Red, pg.Rect(pos[0], pos[1], 10, 10))
    pg.draw.rect(screen_game, Black, pg.Rect(
        prey_location[0], prey_location[1], 10, 10))

    # Conditions to exit Game
    if snake_location[0]<0r snake_location[0] > screen_x-10:
        game_over()
    if snake_location[1]<0 or snake_location[1] > screen_y-10:
        game_over()
    # Looping or Touching body of snake
    for block in body_snake[1:]:
        if snake_location[0] == block[0] and snake_location[1] == block[1]:
            game_over()
    # Call Update score
    update_score(1, Black, 'times new roman', 20)
    # Refresh screen window
    pg.display.update()
    # Update Frame Per Second /Refresh Rate
    frames_ps.tick(snake_moving_speed)
