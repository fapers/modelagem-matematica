import pygame
import random

BACKGROUND_COLOR = (65,105,225)
(WIDTH, HEIGHT) = (400,200)
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PPGMCS - Modelagem Matemática")
SCREEN.fill(BACKGROUND_COLOR)


class Particle:
    def __init__(self, position, size):
        self.x = position[0]
        self.y = position[1]
        self.size = size
        self.colour = (255, 255, 255)
        self.thickness = 0
        
    def display(self):
        pygame.draw.circle(SCREEN, self.colour, (self.x, self.y), self.size, self.thickness)
        

number_of_particles = 100
my_particles = []
for n in range(number_of_particles):
    size = random.randint(10,20)
    x = random.randint(size, WIDTH - size)
    y = random.randint(size, HEIGHT - size)
    my_particles.append(Particle((x,y),size))
    
for particle in my_particles:
    particle.display()
    
pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break
    