from scipy.spatial import Voronoi, voronoi_plot_2d
import pygame
from pygame import gfxdraw
import random
import sys


pygame.init()
all_points = []
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
pygame.display.set_caption("Voronoi Diagram Visualization in Python w/ SciPy & PyGame ")
WIN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))


class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.r = 5
        self.c = (110, 110, 110)

    def update(self):
        self.move()
        self.draw()

    def move(self):
        pass

    def draw(self):
        pygame.gfxdraw.filled_circle(WIN, self.x, self.y, self.r, self.c)


for _ in range(10):
    all_points.append(Point(random.randint(0, WINDOW_WIDTH), random.randint(0, WINDOW_HEIGHT)))
vor = Voronoi([(point.x, point.y) for point in all_points])

running = __name__ == "__main__"
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    WIN.fill((170, 170, 170))
    for point in all_points:
        point.update()
    pygame.display.update()

pygame.quit()
sys.exit()
