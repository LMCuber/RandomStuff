import pygame
from pprint import pprint
from random import randint as rand, uniform as randf
from math import log2
import sys


def ppprint(world):
    print("[")
    for col in world:
        print(f" {col}")
    print("]\n")


def randomness():
    return randf(-10, 10)


def seed():
    return rand(1, 9)


size = 2 ** 10
mult = 1
pygame.init()
pygame.display.set_caption("Diamond-Square Algorithm")
WIN = pygame.display.set_mode((size * mult, size * mult))
cs = size
# dot = "\u2022"
dot = 0
world = [[dot] * (size + 1) for _ in range(size + 1)]
world[0][0] = seed()
world[0][-1] = seed()
world[-1][0] = seed()
world[-1][-1] = seed()
nth = 0
for i in range(int(log2(size))):
    num_squares = 2 ** nth
    for y in range(num_squares):
        for x in range(num_squares):
            # init
            x = int(x)
            cs = int(cs)
            # square step
            points = [world[y * cs][x * cs], world[y * cs][x * cs + cs], world[y * cs + cs][x * cs], world[y * cs + cs][x * cs + cs]]
            avg = sum(points) / len(points) + randomness()
            world[x * cs + cs // 2][y * cs + cs // 2] = avg
            # diamond step
            points = [world[x * cs + cs // 2][y * cs + cs // 2], world[y * cs][x * cs], world[y * cs][x * cs + cs]]
            avg = sum(points) / len(points) + randomness()
            world[y * cs][x * cs + cs // 2] = avg  # top
            points = [world[x * cs + cs // 2][y * cs + cs // 2], world[y * cs][x * cs + cs], world[y * cs + cs][x * cs + cs]]
            avg = sum(points) / len(points) + randomness()
            world[y * cs + cs // 2][x * cs + cs] = avg  # right
            points = [world[x * cs + cs // 2][y * cs + cs // 2], world[y * cs + cs][x * cs + cs], world[y * cs + cs][x * cs]]
            avg = sum(points) / len(points) + randomness()
            world[y * cs + cs][x * cs + cs // 2] = avg  # bottom
            points = [world[x * cs + cs // 2][y * cs + cs // 2], world[y * cs + cs][x * cs], world[y * cs][x * cs]]
            avg = sum(points) / len(points) + randomness()
            world[y * cs + cs // 2][x * cs] = avg  # left
    # next iteration setup
    cs /= 2
    nth += 1
world = [[round(x, 1) if x > 0 else 0 for x in y] for y in world]
highest = max([x for y in world for x in y])
rects = []
for yi, y in enumerate(world):
    for xi, x in enumerate(y):
        base = 1
        color = [base * round(x / highest * 255 / base) + rand(0, 0) for _ in range(3)]
        if max(color) > 255:
            color = [255, 255, 255]
        elif min(color) < 0:
            color = [0, 0, 0]
        rects.append(((xi * mult, yi * mult, mult, mult), color))
        # rects.append(((xi * mult, yi * mult, mult, mult), [rand(0, 255)] * 3))
running = __name__ == "__main__"
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    WIN.fill((100, 100, 100))
    for rect, color in rects:
        pygame.draw.rect(WIN, color, rect)
    pygame.display.update()

pygame.quit()
sys.exit()
