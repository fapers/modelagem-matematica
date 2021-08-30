import pygame
import random

background_colour = (255,0,0)
(width, height) = (400,200)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("PPGMCS - Modelagem Matemática")
screen.fill(background_colour)

# pygame.draw.circle(screen, (0,0,255), (150,100), 30,2)

class Particle:
    def __init__(self, position, size):
        self.x = position[0]
        self.y = position[1]
        self.size = size
        self.colour = (0,0,255)
        self.thickness = 0
        
    def display(self):
        pygame.draw.circle(screen, self.colour, (self.x, self.y), self.size, self.thickness)
        
size = random.randint(10,20)
x = random.randint(size, width - size)
y = random.randint(size, height - size)
my_random_particle = Particle((x,y),size)
my_random_particle.display()

# my_first_particle = Particle((150,100),25)
# my_first_particle.display()

pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
