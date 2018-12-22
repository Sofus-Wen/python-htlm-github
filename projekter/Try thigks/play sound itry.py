import pygame

pygame.init()

surface = pygame.display.set_mode((400, 300))
pic = pygame.image.load("D:/Users/sofus/untitled/bg1.jpg")

surface.blit(pic, (0, 0))
pygame.display.update()
text = input("Press enter to exit.")
