import pygame
import random
import math

backgrond_colour = (255,0,0)
(width, height) = (400,200)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Exemplo 4")
screen.fill(backgrond_colour)

class Particle():
    def __init__(self, position, size):
        self.x = position[0]
        self.y = position[1]
        self.size = size
        self.colour = (0,0,255)
        self.thickness = 1
        self.speed = 0
        self.angle = 0
        
    def display(self):
        pygame.draw.circle(screen, self.colour, (self.x, self.y), self.size, self.thickness)
        
    def move(self):
        self.x += math.sin(self.angle) * self.speed
        self.y -= math.cos(self.angle) * self.speed
        
        
number_of_particles = 100
my_particles = []

for n in range(number_of_particles):
    size = random.randint(10, 20)
    x = random.randint(size, width - size)
    y = random.randint(size, height - size)
    
    particle = Particle((x,y), size)
    particle.speed = random.random()
    particle.angle = random.uniform(0, math.pi*2)
    
    my_particles.append(particle)

clock = pygame.time.Clock()
while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.fill(backgrond_colour)
    
    for particle in my_particles:
        particle.move()
        particle.display()
    pygame.display.flip()
    