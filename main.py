import pygame



pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Fractal 01")

def drawScreen():
    screen.fill((0,0,0))

running = True
while running:
    drawScreen()
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            running = False
        
pygame.quit()
exit(0)