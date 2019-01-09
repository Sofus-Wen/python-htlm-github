import pygame
import subprocess
import os
from pygame.locals import *
import sys

pygame.init()
pygame.display.set_caption('Ping Pong')
subprocess.Popen(['5-Elevator-Music-Royalty-Free.mp3'], shell=True)

current_path = os.path.dirname(__file__) # Where your .py file is located
resource_path = os.path.join(current_path, 'resources') # The resource folder path
image_path = os.path.join(resource_path, 'images') # The image folder path

Height = 1000
Length = 1000
screen = pygame.display.set_mode((Height, Length))
pygame.display.flip()


ball = pygame.image.load(os.path.join(image_path, 'pixil-frame-0.png'))
player_1 = pygame.image.load(os.path.join(image_path, 'player_1-to-ping-pong-pixilart.png'))
player_2 = pygame.image.load(os.path.join(image_path, 'player_2-to-ping-pong-pixilart.png'))

while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        screen.fill((0, 0, 255))
        pygame.display.flip()
        pygame.display.update()