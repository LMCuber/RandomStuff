import pygame
import sys
import opensimplex as osimplex
from time import perf_counter
from math import sin, sqrt


pygame.init()
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
S = 8
t = 0


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        
        elif event.type == pygame.MOUSEMOTION:
            dx, dy = event.rel
            t += dx * 0.003
    
    vel = 0.03 * (sin(perf_counter() * 2) + 1) / 2 + 0.006
    t += vel
    z = t
    m = 0.05
    for y in range(HEIGHT // S):
        for x in range(WIDTH // S):
            n = osimplex.noise3(x=x * m, y=y * m, z=z)
            color = [(n + 1) * 255 / 2] * 3
            if n >= 0.2:
                color = (0, 180, 0)
            elif n >= 0:
                color = (255, 255, 200)
            else:
                color = (0, 120, 120)
            pygame.draw.rect(WIN, color, (x * S, y * S, S, S))
    
    pygame.display.update()
    clock.tick(120)

sys.exit()