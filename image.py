import pygame, random, sys
pygame.init()
url = r"/Users/leonik/Downloads/portrait.jpeg"
old_image = pygame.image.load(url)
image = old_image.copy()
for y in range(old_image.get_height()):
    for x in range(old_image.get_width()):
        rand = 100
        pygame.draw.line(image, old_image.get_at((x, y)), (x, y), (x + random.randint(-rand, rand), y + random.randint(-rand, rand)))
WIN = pygame.display.set_mode(image.get_size())
running = __name__ == "__main__"
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    WIN.fill((0, 0, 0))
    WIN.blit(image, (0, 0))
    pygame.display.update()
pygame.quit()
sys.exit()
