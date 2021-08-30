import pygame

background_colour = (255,0,0)
(width, height) = (1200, 780)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("PPGMCS - Modelagem Matemática")
screen.fill(background_colour)

pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
