import pygame
import sys
import pygame as pygame
from pygame.locals import *

pygame.init()

skrn = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Menu')
skrn.fill((255, 255, 255))
menuAtivo = True

start_button = pygame.draw.rect(skrn, (0, 0, 240), (150, 90, 100, 50))
continue_button = pygame.draw.rect(skrn, (0, 244, 0), (150, 160, 100, 50))
quit_button = pygame.draw.rect(skrn, (244, 0, 0), (150, 230, 100, 50))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        sys_font = pygame.font.SysFont \
            ("None", 60)
        rendered = sys_font.render \
            ('-The Menu-', 0, (0, 0, 0))
        skrn.blit(rendered, (90, 20))
        pygame.display.update()
        while menuAtivo:
            import pygame

            for evento in pygame.event.get():
                print(evento);
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pos()[0] >= 150 and pygame.mouse.get_pos()[1] >= 230:
                        if pygame.mouse.get_pos()[0] <= 250 and pygame.mouse.get_pos()[1] <= 280:
                            pygame.quit();
                    if pygame.mouse.get_pos()[0] >= 150 and pygame.mouse.get_pos()[1] >= 160:
                        if pygame.mouse.get_pos()[0] <= 250 and pygame.mouse.get_pos()[1] <= 210:
                            startKlokken()
                    if pygame.mouse.get_pos()[0] >= 150 and pygame.mouse.get_pos()[1] >= 90:
                        if pygame.mouse.get_pos()[0] <= 250 and pygame.mouse.get_pos()[1] <= 140:
                            startGame();

                    pygame.display.update()