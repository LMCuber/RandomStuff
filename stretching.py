from pygame._sdl2.video import Window, Renderer, Texture
import pygame
import sys


pygame.init()

WIN = Window(size=(1000, 800))
REN = Renderer(WIN)

surf = pygame.image.load("billy.png")
tex = Texture.from_surface(REN, surf)
drect = pygame.Rect((10, 10, 200, 200))
drect = tex.get_rect(topleft=(100, 100))
srect = pygame.Rect((0, 0, 20, 20))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    REN.clear()
    REN.blit(tex, drect, srect)
    REN.present()

pygame.quit()
sys.exit()
