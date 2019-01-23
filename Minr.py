import pygame
import random as r
pygame.init()

w = pygame.display.set_mode((700, 700))

pygame.display.set_caption("Minr")

x = 50
y = 50
width = 70
height = 70
speed = 2

minr = pygame.transform.scale(pygame.image.load("Miner.png"), (width, height))

class Tile:
    color = [0, 0, 0]
    pos = [0, 0]
    def __init__(c,cc,ccc,p,pp):
        color[0] = c
        color[0] = cc
        color[0] = ccc
        pos[0] = p
        pos[1] = pp

tiles = [[[r.randint(0, 1),r.randint(0, 1),r.randint(0, 1)],[r.randint(0, 1),r.randint(0, 1),r.randint(0, 1),r.randint(0, 1)],[r.randint(0, 1),r.randint(0, 1),r.randint(0, 1),r.randint(0, 1)],[r.randint(0, 1),r.randint(0, 1),r.randint(0, 1),r.randint(0, 1)],[r.randint(0, 1),r.randint(0, 1),r.randint(0, 1),r.randint(0, 1)],[r.randint(0, 1),r.randint(0, 1),r.randint(0, 1),r.randint(0, 1)],[r.randint(0, 1),r.randint(0, 1),r.randint(0, 1),r.randint(0, 1)]],
         [[r.randint(0, 1),r.randint(0, 1),r.randint(0, 1),r.randint(0, 1)],[r.randint(0, 1),r.randint(0, 1),r.randint(0, 1),r.randint(0, 1)],[r.randint(0, 1),r.randint(0, 1),r.randint(0, 1),r.randint(0, 1)],[r.randint(0, 1),r.randint(0, 1),r.randint(0, 1),r.randint(0, 1)],[r.randint(0, 1),r.randint(0, 1),r.randint(0, 1),r.randint(0, 1)],[r.randint(0, 1),r.randint(0, 1),r.randint(0, 1),r.randint(0, 1)],[r.randint(0, 1),r.randint(0, 1),r.randint(0, 1),r.randint(0, 1)]],
         [[r.randint(0, 1),r.randint(0, 1),r.randint(0, 1),r.randint(0, 1)],[r.randint(0, 1),r.randint(0, 1),r.randint(0, 1),r.randint(0, 1)],[r.randint(0, 1),r.randint(0, 1),r.randint(0, 1),r.randint(0, 1)],[r.randint(0, 1),r.randint(0, 1),r.randint(0, 1),r.randint(0, 1)],[r.randint(0, 1),r.randint(0, 1),r.randint(0, 1),r.randint(0, 1)],[r.randint(0, 1),r.randint(0, 1),r.randint(0, 1),r.randint(0, 1)],[r.randint(0, 1),r.randint(0, 1),r.randint(0, 1),r.randint(0, 1)]],
         [[r.randint(0, 1),r.randint(0, 1),r.randint(0, 1),r.randint(0, 1)],[r.randint(0, 1),r.randint(0, 1),r.randint(0, 1),r.randint(0, 1)],[r.randint(0, 1),r.randint(0, 1),r.randint(0, 1),r.randint(0, 1)],[r.randint(0, 1),r.randint(0, 1),r.randint(0, 1),r.randint(0, 1)],[r.randint(0, 1),r.randint(0, 1),r.randint(0, 1),r.randint(0, 1)],[r.randint(0, 1),r.randint(0, 1),r.randint(0, 1),r.randint(0, 1)],[r.randint(0, 1),r.randint(0, 1),r.randint(0, 1),r.randint(0, 1)]],
         [[r.randint(0, 1),r.randint(0, 1),r.randint(0, 1),r.randint(0, 1)],[r.randint(0, 1),r.randint(0, 1),r.randint(0, 1),r.randint(0, 1)],[r.randint(0, 1),r.randint(0, 1),r.randint(0, 1),r.randint(0, 1)],[r.randint(0, 1),r.randint(0, 1),r.randint(0, 1),r.randint(0, 1)],[r.randint(0, 1),r.randint(0, 1),r.randint(0, 1),r.randint(0, 1)],[r.randint(0, 1),r.randint(0, 1),r.randint(0, 1),r.randint(0, 1)],[r.randint(0, 1),r.randint(0, 1),r.randint(0, 1),r.randint(0, 1)]],
         [[r.randint(0, 1),r.randint(0, 1),r.randint(0, 1),r.randint(0, 1)],[r.randint(0, 1),r.randint(0, 1),r.randint(0, 1),r.randint(0, 1)],[r.randint(0, 1),r.randint(0, 1),r.randint(0, 1),r.randint(0, 1)],[r.randint(0, 1),r.randint(0, 1),r.randint(0, 1),r.randint(0, 1)],[r.randint(0, 1),r.randint(0, 1),r.randint(0, 1),r.randint(0, 1)],[r.randint(0, 1),r.randint(0, 1),r.randint(0, 1),r.randint(0, 1)],[r.randint(0, 1),r.randint(0, 1),r.randint(0, 1),r.randint(0, 1)]],
         [[r.randint(0, 1),r.randint(0, 1),r.randint(0, 1),r.randint(0, 1)],[r.randint(0, 1),r.randint(0, 1),r.randint(0, 1),r.randint(0, 1)],[r.randint(0, 1),r.randint(0, 1),r.randint(0, 1),r.randint(0, 1)],[r.randint(0, 1),r.randint(0, 1),r.randint(0, 1),r.randint(0, 1)],[r.randint(0, 1),r.randint(0, 1),r.randint(0, 1),r.randint(0, 1)],[r.randint(0, 1),r.randint(0, 1),r.randint(0, 1),r.randint(0, 1)],[r.randint(0, 1),r.randint(0, 1),r.randint(0, 1),r.randint(0, 1)]]]

run = True
while run:
    pygame.time.delay(10)

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 0:
        x-=speed
    if keys[pygame.K_RIGHT] and x < 700-width:
        x+=speed
    if keys[pygame.K_UP] and y > 0:
        y-=speed
    if keys[pygame.K_DOWN] and y < 700 -height:
        y+=speed

    w.fill(0)

    for i in range(0,7):
        for j in range(0,7):
            pygame.draw.rect(w, (tiles[i][j][0]*255, tiles[i][j][1]*255, tiles[i][j][2]*255), (i*100, j*100, 100, 100))
        
    
    w.blit(minr, (x, y))
    pygame.display.update();
pygame.quit()
