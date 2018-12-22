import pygame

pygame.init()

screen = pygame.display.set_mode((400, 300))
clock = pygame.time.Clock()
done = False

font = pygame.font.SysFont("comicsansms", 72)

text = font.render("Menu", True, (0, 128, 0))

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True

    screen.fill((255, 255, 255))
    screen.blit(text,
                (200 - text.get_width() // 2, 50 - text.get_height() // 2))

    pygame.display.flip()
    clock.tick(60)