import pygame
import time
pygame.init()
okno = pygame.display.set_mode((800, 800))
x = 100
y = 100
dol = True
pygame.display.set_caption("Witam")
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    okno.fill([100,150,100])
    pygame.draw.circle(okno, [0,0,200], (x,y),50)
    #pygame.draw.rect(okno, [255,255,255], pygame.Rect(100,100,150,550))
    #pygame.draw.polygon(okno,[255,0,0],[[130,100],[460,380],[700,810]])
    pygame.display.update()
    if y < 800 and dol:
        y += 0.5
    if y == 800:
        dol = False
    if y > 100 and dol == False:
        y -= 0.5
    if y == 100:
        dol = True
pygame.quit()