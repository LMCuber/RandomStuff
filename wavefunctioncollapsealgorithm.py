import pygame
import sys
import random
from contextlib import suppress
from pprint import pprint


def get_neis(arr, y, x):
    neis = []
    #
    if x > 0:
        neis.append(arr[y][x - 1])
    if y > 0:
        neis.append(arr[y - 1][x])
    if x < len(row) - 1:
        neis.append(arr[y][x + 1])
    if y < len(ref) - 1:
        neis.append(arr[y + 1][x])
    # if  > 0 and y > 0:
        # neis.append(arr[y - 1][x - 1])
    # if x < len(row) - 1 and y > 0:
        # neis.append(arr[y - 1][x + 1])
    # if x < len(row) - 1 and y < len(ref) - 1:
        # neis.append(arr[y + 1][x + 1])
    # if x > 0 and y < len(ref) - 1:
        # neis.append(arr[y + 1][x - 1])
    return neis


pygame.init()
pygame.display.set_caption("Wave Function Collapse Algorithm")
BS = 18
W, H = 30, 30
WIN = pygame.display.set_mode((BS * W, BS * H))
clock = pygame.time.Clock()

color_map = {0: (255, 255, 255),
             1: (0, 0, 0),
             2: (255, 0, 0),
}
ref = [
    [0, 0, 0, 0],
    [0, 1, 1, 1],
    [0, 1, 2, 1],
    [0, 1, 2, 1],
]
level = [[None for x in range(W)] for y in range(H)]

neighbors = {}
for y, row in enumerate(ref):
    for x, block in enumerate(row):
        neis = get_neis(ref, y, x)
        #
        if block in neighbors:
            neighbors[block].extend(neis)
        else:
            neighbors[block] = neis
neighbors = {k: list(set(v)) for k, v in neighbors.items()} | {None: (0, 1, 2)}

for y, row in enumerate(level):
    for x, block in enumerate(row):
        level[y][x] = random.choice((0, 1, 2))

running = __name__ == "__main__"
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    WIN.fill((120, 120, 120))
    for y, row in enumerate(level):
        for x, block in enumerate(row):
            color = color_map.get(block, (120, 120, 120))
            pygame.draw.rect(WIN, color, (x * BS, y * BS, BS, BS))
    pygame.display.update()

pygame.quit()
sys.exit()
