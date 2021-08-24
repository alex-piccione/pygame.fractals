import pygame
import random
from math import sin, cos, radians

WIDTH, HEIGHT = 1200,960
pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fractal 01")

x,y = WIDTH/2, HEIGHT-100

def inScreen(x,y):
    return (x >+ 0 and x <= WIDTH) and (y >= 0 and y <= HEIGHT)

def lighter(color, step):
    (r,g,b) = color
    def increase(v): return min(v+step*15, 255)
    return (increase(r), increase(g), increase(b))


def addRandomness(color, step):
    (r,g,b) = color
    def f(v): return max(min(v+random.randrange(-100, +100), 255), 0)
    return (f(r), f(g), f(b))

def drawBranches(ends, step, color):

    if step > 25 or len(ends) > 1500: return

    angle_deviation = 15
    start_length = 30 - (step*2.5)
    
    length = start_length*(step*1.5)
    if length < 5: return

    color = lighter(color, step)
    color = addRandomness(color, step)
    #print(color)
    new_ends = []

    width = 1 #random.randrange(1,10)

    for end in ends:  
        (x1, y1), angle = end 

        # left
        new_angle = angle - angle_deviation
        x2 = x1 + int(cos(radians(new_angle)) * length)
        y2 = y1 + int(sin(radians(new_angle)) * length)
        if inScreen(x2, y2):
            new_ends.append( ((x2, y2), new_angle))
        pygame.draw.line(screen, color, (x1, y1), (x2, y2), width)

        # right
        new_angle = angle + angle_deviation
        x2 = x1 + int(cos(radians(new_angle)) * length)
        y2 = y1 + int(sin(radians(new_angle)) * length)
        if inScreen(x2, y2):
            new_ends.append( ((x2, y2), new_angle))
        pygame.draw.line(screen, color, (x1, y1), (x2, y2), width)
        
    pygame.display.update()
    pygame.time.delay(10)

    drawBranches(new_ends, step+1, color)

center = (WIDTH/2, HEIGHT/2)
start_color = (0, 0, 0)
start_angle = 0 # required to have Up as start direction
n_parts = 3 # how many



running = True
while running:
    #screen.fill((0,0,0))
    angle = start_angle + 360/n_parts
    if angle > 360:
        angle = 0
        screen.fill((0,0,0))
    drawBranches( [(center, angle)], 1, start_color)
    pygame.time.delay(10)
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            running = False
        
pygame.quit()
exit(0)