import pygame

background_colour = (255,0,0)
(width, height) = (400, 200)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("PPGMC - Modelagem Matemática")
screen.fill(background_colour)

class Circle:
    def __init__(self, position, size):
        self.x = position[0]
        self.y = position[1]
        
        self.size = size
        self.colour = (0,255,0)
        self.thickness = 25
    
    def display(self):
        pygame.draw.circle(screen, self.colour, (self.x, self.y), self.size, self.thickness)
        
ball_one = Circle((150,100), 25)
ball_one.display()

class Square:
    def __init__(self, position, size, thickness):
        self.x1 = position[0]
        self.y1 = position[1]
        self.x2 = size[0]
        self.y2 = size[1]
        
        self.colour = (0,0,255)
        self.thickness = thickness
    
    def display(self):
        pygame.draw.rect(screen, self.colour, (self.x1, self.y1, self.x2, self.y2), self.thickness)

square_one = Square((50,50), (100,100), 1)
square_one.display()

pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
