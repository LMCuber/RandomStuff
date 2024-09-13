import matplotlib.pyplot as plt
import numpy as np
from math import e
#import pygame
import sys


def get_complex(x, y):
    r = x / WIDTH * 4 - 2
    i = y / HEIGHT * 4 - 2
    c = complex(r, i)
    return c


def get_coord(c):
    r, i = c.real, c.imag
    x = int(r * WIDTH / 4 + WIDTH / 2)
    y = int(i * HEIGHT / 4 + HEIGHT / 2)
    return x, y



WIDTH, HEIGHT = 500, 500
"""
pygame.init()
pygame.display.set_caption("Fractal")
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
"""

BLACK = (0, 0, 0)
GRAY = (150, 150, 150)
pixel_array = [[None] * WIDTH for _ in range(HEIGHT)]

f = lambda z: z ** 2 + c

Break = type("Break", (Exception,), {})

for y in range(HEIGHT):
    for x in range(WIDTH):
        try:
            c = get_complex(x, y)
            been = []
            n = 0
            for _ in range(20):
                n = f(n)
                if abs(n) >= 100:
                    raise Break
                been.append(n)
            raise Break
        except Break:
            n = len(been)
            color = [255 - n // 20 * 255] * 3
            pixel_array[y][x] = color
            #WIN.set_at((x, y), color)

"""
running = __name__ == "__main__"
while running:
    WIN.fill((0, 0, 0))
    for oindex, y in enumerate(pixel_array):
        for iindex, color in enumerate(y):
            WIN.set_at((iindex, oindex), color)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()
sys.exit()
"""

plt.imshow(pixel_array, extent=[-2, 2, -2, 2])
plt.show()
