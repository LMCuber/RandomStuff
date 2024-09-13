import pygame, random
pygame.init()
pygame.display.set_caption("lmoa")
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
WIN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break
    for y in range(WINDOW_HEIGHT):
        for x in range(WINDOW_WIDTH):
            WIN.set_at((x, y), [random.randint(0, 255) for _ in range(3)])
    pygame.display.update()
pygame.quit()
raise SystemExit
