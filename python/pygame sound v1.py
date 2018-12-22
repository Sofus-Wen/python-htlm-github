import pygame

import time

pygame.init()

pygame.mixer.music.set_volume(6.0)

pygame.mixer.music.load("D:\\sofus\\Overførelser\\foo.mp3")

pygame.mixer.music.play()

time.sleep(10)