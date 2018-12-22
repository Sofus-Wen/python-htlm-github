import pygame

# It starts here js
pygame.init();
screen = pygame.display.set_mode((400, 300));
pygame.display.set_caption('Menu')
# bg_1 = pygame.image.load('bg1.jpg')
menuAtivo = True;
screen.fill((250, 235, 215));

start_button = pygame.draw.rect(screen, (0, 0, 240), (150, 90, 100, 50));
continue_button = pygame.draw.rect(screen, (0, 244, 0), (150, 160, 100, 50));
quit_button = pygame.draw.rect(screen, (244, 0, 0), (150, 230, 100, 50));

pygame.display.flip();


def startGame():
    Spil_1()


def startKlokken():
    Klokken()


while menuAtivo:
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
