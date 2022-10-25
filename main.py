import pygame
import pygame.gfxdraw

WIDTH, HEIGHT = 1000, 600
WIN = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Pong")
FPS = 30
clock = pygame.time.Clock()
PADDLE_HEIGHT = 100
PADDLE_WIDTH = 20
top_left = HEIGHT//2 - PADDLE_HEIGHT//2
top_right = HEIGHT//2 - PADDLE_HEIGHT//2
ball_x = WIDTH//2
ball_y = HEIGHT//2
ball_size = 7
vel = 7

def draw_win():
    WIN.fill((0, 0, 0))
    pygame.gfxdraw.filled_polygon(WIN, ((25, top_left), (25, top_left+PADDLE_HEIGHT), (25+PADDLE_WIDTH, top_left+PADDLE_HEIGHT), (25+PADDLE_WIDTH, top_left)), (255, 255, 255))
    pygame.gfxdraw.filled_polygon(WIN, ((WIDTH - 50, top_right), (WIDTH - 50, top_right+PADDLE_HEIGHT), (WIDTH - 50+PADDLE_WIDTH, top_right+PADDLE_HEIGHT), (WIDTH - 50+PADDLE_WIDTH, top_right)), (255, 255, 255))
    pygame.gfxdraw.line(WIN, WIDTH//2, 0, WIDTH//2, HEIGHT, (255, 255, 255))
    pygame.gfxdraw.filled_polygon(WIN, ((ball_x-ball_size, ball_y-ball_size), (ball_x-ball_size, ball_y+ball_size), (ball_x+ball_size, ball_y+ball_size), (ball_x+ball_size, ball_y-ball_size)), (255, 255, 255))
    pygame.display.update()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        top_left -= 5
    elif keys[pygame.K_s]:
        top_left += 5

    if keys[pygame.K_UP]:
        top_right -= 5
    elif keys[pygame.K_DOWN]:
        top_right += 5


    draw_win()
    clock.tick(FPS)

pygame.quit()
