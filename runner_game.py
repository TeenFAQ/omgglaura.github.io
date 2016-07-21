import pygame
import random
from city_scroller import Scroller as Scroller
import os, sys

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (129, 129, 129)
YELLOW = (255, 255, 0)
colors = [BLACK, GREEN, BLUE, RED, YELLOW]

FRONT_SCROLLER_COLOR = (0,0,30)
MIDDLE_SCROLLER_COLOR = (30,30,100)
BACK_SCROLLER_COLOR = (50,50,150)
BACKGROUND_COLOR = (17, 9, 89)

def random_color():
    return random.choice(colors)

# initialize the pygame class
pygame.init()

# Set the width and height of the screen [width, height]
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set the title of the window
pygame.display.set_caption("Runner Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

class RunnerSprite(object):
    def __init__(self, size):
        #pygame.sprite.Sprite.__init__(self)
        self.image_a = pygame.image.load("pug.png").convert()
        self.image_b = self.image_a.get_rect()
        self.size = size
        self.x = 0
        self.y = 500
        self.image_a.set_colorkey(BLUE)

    #def mouse_position(self):
        #self.move(self.x, self.y)

    def draw(self, screen):
        screen.blit(self.image_a, (self.x, self.y))


    #def CheckCollision(self)
        #if pygame.sprite.collide_rect(pug, donut)

class Food(object):
    def __init__(self, size):
        #pygame.sprite.Sprite.__init__(self)
        self.image_a = pygame.image.load("hamburgernew.png").convert()
        self.image_b = self.image_a.get_rect()
        self.size = size
        self.x = 500
        self.y = 500
        self.image_a.set_colorkey(BLUE)

    #def mouse_position(self):
        #self.move(self.x, self.y)

    def draw(self, screen):
        screen.blit(self.image_a, (self.x, self.y))


    #def CheckCollision(self)
        #if pygame.sprite.collide_rect(pug, donut)
       
        
#all_sprites_list = pygame.sprite.Group()

pug = RunnerSprite(1)
hamburger = Food(1)

#all_sprites_list.add(pug)

front_scroller = Scroller(SCREEN_WIDTH, 400, SCREEN_HEIGHT, FRONT_SCROLLER_COLOR, 3, screen)
middle_scroller = Scroller(SCREEN_WIDTH, 200, (SCREEN_HEIGHT - 50), MIDDLE_SCROLLER_COLOR, 2, screen)
back_scroller = Scroller(SCREEN_WIDTH, 20, (SCREEN_HEIGHT - 100), BACK_SCROLLER_COLOR, 1, screen)

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BACKGROUND_COLOR)

    # --- Drawing code should go here
    back_scroller.draw_buildings()
    back_scroller.move_buildings()
    middle_scroller.draw_buildings()
    middle_scroller.move_buildings()
    front_scroller.draw_buildings()
    front_scroller.move_buildings()
    #all_sprites_list.draw(screen)
    #pug.mouse_position()
    pug.draw(screen)
    hamburger.draw(screen)
    

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE
