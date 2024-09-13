import pygame
import sys
import math


def get_vel(src, dest):
    dx = dest[0] - src[0]
    dy = dest[1] - src[1]
    angle = math.atan2(dy, dx)
    xvel = math.cos(angle)
    yvel = math.sin(angle)
    return xvel, yvel


pygame.init()


pygame.display.set_caption("4 Objects")
WIN = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

s = 20
object1 = [50, 50, 10]
object2 = [450, 50, 10]
object3 = [450, 450, 10]
object4 = [50, 450, 10]

running = __name__ == "__main__"
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    WIN.fill((50, 50, 50))

    xvel, yvel = get_vel(object1, object2)
    object1[0] += xvel
    object1[1] += yvel
    pygame.draw.rect(WIN, (120, 120, 120), [*object1[:2], s, s])
    xvel, yvel = get_vel(object2, object3)
    object2[0] += xvel
    object2[1] += yvel
    pygame.draw.rect(WIN, (120, 120, 120), [*object2[:2], s, s])
    xvel, yvel = get_vel(object3, object4)
    object3[0] += xvel
    object3[1] += yvel
    pygame.draw.rect(WIN, (120, 120, 120), [*object3[:2], s, s])
    xvel, yvel = get_vel(object4, object1)
    object4[0] += xvel
    object4[1] += yvel
    pygame.draw.rect(WIN, (120, 120, 120), [*object4[:2], s, s])

    pygame.display.update()

pygame.quit()
sys.exit()
