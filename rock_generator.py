from pyengine.pgbasics import *
from scipy.spatial import Delaunay, ConvexHull
from pprint import pprint


#
WIDTH, HEIGHT = 800, 600
WIN = Window(size=(WIDTH, HEIGHT), title="Procedural Rock Generator")
REN = Renderer(WIN)
#
vertices = []
n = 10
m = 150
for _ in range(n):
    vertices.append([randf(-1, 1), randf(-1, 1), 0])

pprint(vertices)

print("-"*20)


triangles = Delaunay([v[:2] for v in vertices])

pprint(triangles)

fill_colors = [rgb_mult(LIGHT_GRAY, randf(0.9, 1.1)) for _ in triangles.simplices]
rock = Crystal(
    REN,
    vertices,
    [RED] * n, [

    ], [
        # [[LIGHT_GRAY, YELLOW], 0, 1, 2, 3]
    ],
    (WIDTH / 2, HEIGHT / 2), m, 4, 0, 0, 0, 0, 0.01, 0, rotate=False

)
#
clock = pygame.time.Clock()
running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    rock.update()
    fill_rect(REN, DARK_GRAY, (0, 0, WIDTH, HEIGHT))
    final = []
    for i, tri in enumerate(triangles.simplices):
        points = [rock.circles[i][1] for i in tri]
        fill_triangle(REN, fill_colors[i], *points)
        final.extend([p.center for p in points])
    """
    cv_hull = ConvexHull(final).vertices
    for i in range(len(cv_hull)):
        try:
            cur, nex = cv_hull[i], cv_hull[i + 1]
        except IndexError:
            cur, nex = cv_hull[i], cv_hull[0]
        finally:
            src = final[cur]
            dest = final[nex]
            draw_line(REN, YELLOW, src, dest)
    """

    # print(cv_hull)
    draw_rect(REN, RED, (WIDTH / 2 - m, HEIGHT / 2 - m, m * 2, m * 2))
    REN.present()

pygame.quit()
sys.exit()
