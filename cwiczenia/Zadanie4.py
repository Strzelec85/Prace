import pygame
import time

okno = pygame.display.set_mode([400,300])
pygame.display.set_caption("Tekst")

pygame.font.init()
czcionka = pygame.font.SysFont("Comic Sans MS", 50)

i = 60
'''
napis2 = czcionka.render("Witaj świecie", False, [0,0,255])

okno.blit(napis2, [0,60])
'''

running = True
while running:
    n = str(i)

    kolo = pygame.draw.circle(okno, [255, 255, 255], [200, 150], 100)
    if i > 0:
        i -= 1
    napis = czcionka.render(n, True, [0, 0, 255])
    okno.blit(napis, [170, 110])
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    time.sleep(0.5)
pygame.quit()