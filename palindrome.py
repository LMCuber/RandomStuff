import pygame
import pygame.gfxdraw
import sys

pygame.init()
pygame.display.set_caption("Palindrome")
WIDTH, HEIGHT = 1000, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))


def palindrome(num):
    iter = 0
    while str(num) != str(num)[::-1]:
        num += int(str(num)[::-1])
        iter += 1
        if iter >= 100:
            return -1
    return iter


ys = []
for x in range(WIDTH):
    ys.append(palindrome(x))
running = __name__ == "__main__"
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    WIN.fill((40, 40, 40))
    for x, y in enumerate(ys):
        pygame.gfxdraw.vline(WIN, x, HEIGHT - y * 15, HEIGHT, (120, 120, 120))
    pygame.display.update()

pygame.quit()
sys.exit()
    