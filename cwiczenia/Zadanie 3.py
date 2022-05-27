import pygame
import random
import time

okno = pygame.display.set_mode((727, 484))
pygame.display.set_caption("Obrazy")

i=1

running = True
while running:
    if i == 1:
        i=2
    else:
        i=1
    obrazek = pygame.image.load(f"Kunio{i}.png")
    okno.blit(obrazek, [0, 0])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    time.sleep(1)
    pygame.display.flip()

pygame.quit()