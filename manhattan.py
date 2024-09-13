import pygame
import pygame.gfxdraw
import sys
from math import sqrt
import threading


pygame.init()
WIN = pygame.display.set_mode((800, 600))
pygame.display.set_caption("(Non-)Euclidean Bisectors")
running = True
clock = pygame.time.Clock()

points = [[100, 100], [300, 300]]
man_locus = []
euc_locus = []


dx_a = abs(100 - 460)
dy_a = abs(200 - 80)

dx_b = abs(600 - 460)
dy_b = abs(420 - 80)


def get_locus():
    man_locus.clear()
    euc_locus.clear()
    for y in range(0, 600, 1):
        for x in range(0, 800, 1):
            dx_a = abs(x - points[0][0])
            dy_a = abs(y - points[0][1])
            dx_b = abs(x - points[1][0])
            dy_b = abs(y - points[1][1])
            euc_a = round(sqrt(dx_a ** 2 + dy_a ** 2))
            euc_b = round(sqrt(dx_b ** 2 + dy_b ** 2))
            man_a = dx_a + dy_a
            man_b = dx_b + dy_b
            # print(x, y)
            if man_a == man_b:
                man_locus.append([x, y])
            if euc_a == euc_b:
                euc_locus.append([x, y])

current = None
threading.Thread(target=get_locus).start()
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for index, point in enumerate(points):
                    dx = abs(point[0] - pygame.mouse.get_pos()[0])
                    dy = abs(point[1] - pygame.mouse.get_pos()[1])
                    if dx <= 5 and dy <= 5:
                        current = index
                dx = abs(points[0][0] - pygame.mouse.get_pos()[0])
                dy = abs(points[0][1] - pygame.mouse.get_pos()[1])
                dx2 = abs(points[1][0] - pygame.mouse.get_pos()[0])
                dy2 = abs(points[1][1] - pygame.mouse.get_pos()[1])
                print(pygame.mouse.get_pos())

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                if current is not None:
                    points[current] = [10 * round(p / 10) for p in points[current]]
                if current is not None:
                    threading.Thread(target=get_locus).start()
                current = None

        # elif event.type == pygame.MOUSEMOTION:
        #     if current is not None:
        #         threading.Thread(target=get_locus).start()

    if current is not None:
        points[current] = pygame.mouse.get_pos()

    WIN.fill((40, 40, 40))

    pygame.draw.line(WIN, (230, 230, 230), *points)
    pygame.gfxdraw.filled_circle(WIN, *points[0], 5, (255, 255, 255))
    pygame.gfxdraw.filled_circle(WIN, *points[1], 5, (255, 255, 255))

    for point in euc_locus:
        pygame.gfxdraw.filled_circle(WIN, *point, 1, (0, 255, 0))

    for point in man_locus:
        pygame.gfxdraw.filled_circle(WIN, *point, 3, (255, 0, 0))

    pygame.display.update()

pygame.quit()
sys.exit()
