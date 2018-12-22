import pygame

# from pygame.locals import *

pygame.init()

#Skærmens størelse
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])

running = True

# Our main loop!
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            # If the Esc key has been pressed set running to false to exit the main loop
            if event.key == K_ESCAPE:
                running = False
        # Check for QUIT event; if QUIT, set running to false
        elif event.type == QUIT:
            running = False