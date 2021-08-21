import pygame
from math import sin, cos, radians

WIDTH, HEIGHT = 800,600
pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fractal 01")

x,y = WIDTH/2, HEIGHT-100

def drawScreen():
    screen.fill((0,0,0))
    drawTree(x,y, 0, 8)


def drawTree(x1, y1, angle, depth):
    fork_angle = 30
    base_len = 10
    if depth > 0:
        x2 = x1 + int(cos(radians(angle-90)) * depth * base_len)
        y2 = y1 + int(sin(radians(angle-90)) * depth * base_len)
        pygame.draw.line(screen, (0, 255, 0), (x1, y1), (x2, y2), 2)
        #pygame.time.delay(10)
        pygame.display.update()
        pygame.time.delay(10)
        
        # left and right branch
        drawTree(x2,y2, angle-fork_angle, depth-1)
        drawTree(x2,y2, angle+fork_angle, depth-1)


running = True
while running:
    screen.fill((0,0,0))
    drawScreen()
    pygame.time.delay(5000)
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            running = False
        
pygame.quit()
exit(0)