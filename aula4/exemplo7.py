from exemplo8 import collide
import pygame
import random
import math

backgrond_colour = (65,105,225)
(width, height) = (1200,720)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Exemplo 6")
screen.fill(backgrond_colour)

drag = 0.2
elasticity = 0.75
gravity = (math.pi, 0.5)

def addVectors(vector1, vector2):
    angle1, length1 = vector1
    angle2, length2 = vector2
    x = math.sin(angle1) * length1 + math.sin(angle2) * length2
    y = math.cos(angle1) * length1 + math.cos(angle2) * length2
    length = math.hypot(x, y)
    angle = 0.5 * math.pi - math.atan2(y, x)
    return (angle, length)

def findParticle(particles, x, y):
    for p in particles:
        if math.hypot(p.x - x, p.y - y) <= p.size:
            return p
    return None

class Particle:
    def __init__(self, position, size):
        self.x = position[0]
        self.y = position[1]
        self.size = size
        self.colour = (255,255,255)
        self.thickness = 1
        self.speed = 0
        self.angle = 0
        
    def display(self):
        pygame.draw.circle(screen, self.colour, (self.x, self.y), self.size, self.thickness)
        
    def move(self):
        (self.angle, self.speed) = addVectors((self.angle, self.speed), gravity)
        self.x += math.sin(self.angle) * self.speed
        self.y -= math.cos(self.angle) * self.speed
        self.speed *= drag
        
    def bounce(self):
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
            
        
number_of_particles = 10
my_particles = []

for n in range(number_of_particles):
    size = random.randint(20, 50)
    x = random.randint(size, width - size)
    y = random.randint(size, height - size)    
    
    particle = Particle((x,y), size)
    particle.speed = random.random()
    particle.angle = random.uniform(0, math.pi*2)
    
    my_particles.append(particle)

selected_particle = None
clock = pygame.time.Clock()
while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            (mouseX, mouseY) = pygame.mouse.get_pos()
            selected_particle = findParticle(my_particles, mouseX, mouseY)
        elif event.type == pygame.MOUSEBUTTONUP:
            selected_particle = None
            
    if selected_particle:
        (mouseX, mouseY) = pygame.mouse.get_pos()
        dx = mouseX - selected_particle.x
        dy = mouseY - selected_particle.y
        selected_particle.angle = 0.5*math.pi + math.atan2(dy, dx)
        selected_particle.speed = math.hypot(dx, dy) * 0.1
            
    screen.fill(backgrond_colour)
    
    for particle in my_particles:        
        particle.move()
        particle.bounce()
        particle.display()
        
    pygame.display.flip()
    