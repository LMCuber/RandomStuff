import pygame
import sys
import random
pygame.init()

pygame.display.set_caption("Cake")
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
WIN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
running = __name__ == "__main__"
truthy = faulty = 0
font = pygame.font.SysFont("Comic Sans", 40)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    c1 = random.randint(0, WINDOW_WIDTH)
    c2 = random.randint(0, WINDOW_WIDTH)
    k = random.randint(0, WINDOW_WIDTH)
    WIN.fill((120, 120, 120))
    pygame.draw.rect(WIN, (0, 0, 120), (c1, 100, 20, 100))
    pygame.draw.rect(WIN, (0, 0, 220), (c2, 100, 20, 100))
    pygame.draw.rect(WIN, (200, 200, 200), (k, 100, 20, 100))
    if c1 <= k <= c2 or c2 <= k <= c1:
        truthy += 1
    else:
        faulty += 1
    surf = font.render(f"{truthy} / {truthy + faulty} = {round(truthy / (truthy + faulty), 5)}", False, (0, 0, 0))
    WIN.blit(surf, (WINDOW_WIDTH / 2 - surf.get_width() / 2, 400))
    pygame.display.update()
pygame.quit()
sys.exit()
