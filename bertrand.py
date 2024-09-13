import pygame
import pygame.gfxdraw
import random
import math
import sys
from contextlib import suppress


pygame.init()

WIDTH, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bertrand's Paradox")

point = [WIDTH / 2, HEIGHT / 2]
angle = math.radians(random.randint(0, 360))

circle_surf = pygame.Surface((WIDTH // 2, HEIGHT / 2), pygame.SRCALPHA)
pygame.draw.circle(circle_surf, (240, 240, 240), (WIDTH // 4, HEIGHT // 4), WIDTH // 4, 2)
circle_mask = pygame.mask.from_surface(circle_surf)
point_surf = pygame.Surface((1, 1))
point_surf.fill((180, 180, 180))
point_mask = pygame.mask.from_surface(point_surf)
points_left = 2
points_to_draw = []
lines_to_draw = []
gt = lt = 0
lengths = []
avg = 0
clock = pygame.time.Clock()
b_font = pygame.font.SysFont("Calibri", 50)
s_font = pygame.font.SysFont("Calibri", 35)

running = __name__ == "__main__"
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if points_left > 0:
        point[0] += math.cos(angle)
        point[1] += math.sin(angle)
        circle_pos = (WIDTH / 2 - circle_surf.get_width() / 2, HEIGHT / 2 - circle_surf.get_height() / 2)
        offset = (int(point[0] - circle_pos[0]), int(point[1] - circle_pos[1]))
        if circle_mask.overlap(point_mask, offset):
            points_to_draw.append(point)
            point = [WIDTH / 2, HEIGHT / 2]
            points_left -= 1
            angle = math.radians(random.randint(0, 360))
            if lines_to_draw and points_to_draw and len(points_to_draw) % 2 == 0:
                lines = ([int(p) for p in points_to_draw[-2]], [int(p) for p in points_to_draw[-1]])
                dx, dy = abs(lines[0][0] - lines[1][0]), abs(lines[0][1] - lines[1][1])
                hyp = math.hypot(dy, dx)
                if hyp > 200 * math.sqrt(3):
                    gt += 1
                else:
                    lt += 1
                lengths.append(hyp)
                avg = round(sum(lengths) / len(lengths)) / 200
    WIN.fill((50, 50, 50))
    pygame.draw.rect(WIN, (240, 240, 240), (WIDTH / 2 - circle_surf.get_width() / 2, HEIGHT / 2 - circle_surf.get_height() / 2, *circle_surf.get_size()), 1)
    WIN.blit(circle_surf, (WIDTH / 2 - circle_surf.get_width() / 2, HEIGHT / 2 - circle_surf.get_height() / 2))
    WIN.blit(point_surf, point)
    # for p in points_to_draw:
    #     pygame.draw.circle(WIN, (180, 180, 180), p, 5)
    # for l in lines_to_draw:
    #     pygame.gfxdraw.line(WIN, *l[0], *l[1], (200, 200, 200))
    if points_to_draw and len(points_to_draw) % 2 == 0:
        lines = ([int(p) for p in points_to_draw[-2]], [int(p) for p in points_to_draw[-1]])
        lines_to_draw.append(lines)
        points_left = 2
    with suppress(ZeroDivisionError):
        render_surf = b_font.render(f"{gt}/{lt + gt} = {round(gt / (lt + gt), 3)}", True, (240, 240, 240))
        WIN.blit(render_surf, (WIDTH / 2 - render_surf.get_width() / 2, HEIGHT - 160))
        render_surf = s_font.render(f"Avg: {avg}", True, (240, 240, 240))
        WIN.blit(render_surf, (WIDTH / 2 - render_surf.get_width() / 2, HEIGHT - 105))
    pygame.display.update()

pygame.quit()
sys.exit()
