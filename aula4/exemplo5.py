import pygame
import random
import math

backgrond_colour = (65,105,225)
(width, height) = (1200,720)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Exemplo 5")
screen.fill(backgrond_colour)

drag = 0.0
elasticity = 0.0
gravity = (math.pi, 0.0)

class Particle():
    def __init__(self, position, size):
        self.x = position[0]
        self.y = position[1]
        self.size = size
        self.colour = (255,255,255)
        self.thickness = 1
        
    def move(self):
        self.speed = 10
        self.angle = math.pi / 4
        
        self.x += math.sin(self.angle) * self.speed
        self.y -= math.cos(self.angle) * self.speed
        
        self.direcao = 1
        if self.bounce():
            self.speed = -10
        else:
            self.speed = 10
        
    def bounce(self):
        retorno = 0
        if self.x > width - self.size:
            self.x = 2 * (width - self.size) - self.x
            self.angle = -self.angle
            self.speed *= elasticity
            retorno = 1
        elif self.x < self.size:
            self.x = 2 * self.size - self.x
            self.angle = - self.angle
            self.speed *= elasticity
            retorno = -1
        
        if self.y > height - self.size:
            self.y = 2 * (height - self.size) - self.y
            self.angle = math.pi - self.angle
            self.speed *= elasticity
        elif self.y < self.size:
            self.y = 2 * self.size - self.y
            self.angle = math.pi - self.angle
            self.speed *= elasticity
        return retorno
        
    def display(self):
        pygame.draw.circle(screen, self.colour, (self.x, self.y), self.size, self.thickness)    
        
        
number_of_particles = 1
my_particles = []

for n in range(number_of_particles):
    size = random.randint(10, 20)
    x = random.randint(size, width - size)
    y = random.randint(size, height - size)    
    my_particles.append(Particle((x,y),size))

for particle in my_particles:
    particle.display()
pygame.display.flip()

clock = pygame.time.Clock()
while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.fill(backgrond_colour)
    
    for particle in my_particles:
        # particle.bounce()
        particle.move()        
        particle.display()
    pygame.display.flip()
    