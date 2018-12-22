import time
import pygame
import play
import pymedia

while True:
    højre = (" /(ಠ益ಠ)/ ")
    venstre = (" \(ಠ益ಠ)\ ")
    skip_1 = time.sleep(1)
    skip_2 = time.sleep(0.1)

    play ("Nightcore - Rockefeller Street - (Lyrics).wav")

    pygame.mixer.init()
    pygame.mixer.music.load("Nightcore - Rockefeller Street - (Lyrics).wav")
    pygame.mixer.music.play()
    time.sleep(33)
    print(højre)
    skip_1
    print(venstre)
    skip_1
    print(højre)
    skip_1
    print(højre)
    skip_1
    print(venstre)
    skip_1
    print(højre)
    skip_1
    print(venstre)
    skip_1
    print(venstre)
