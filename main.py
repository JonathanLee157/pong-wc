import pygame
import pygame.gfxdraw

WIDTH, HEIGHT = 1000, 600
WIN = pygame.display.set_mode([WIDTH, HEIGHT])
FPS = 30
clock = pygame.time.Clock()
PADDLE_HEIGHT = 100
PADDLE_WIDTH = 20
top = HEIGHT//2 - PADDLE_HEIGHT//2

def draw_win():
    WIN.fill((0, 0, 0))
    pygame.gfxdraw.filled_polygon(WIN, ((25, top), (25, top+PADDLE_HEIGHT), (25+PADDLE_WIDTH, top+PADDLE_HEIGHT), (25+PADDLE_WIDTH, top)), (255, 255, 255))
    pygame.display.update()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    draw_win()
    clock.tick(FPS)

pygame.quit()
