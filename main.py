import pygame
from constants import *
from block import Block


def draw_block(obj):
    pygame.draw.rect(WIN, obj.color, obj.get_rect())


pygame.init()

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Collision Simulation")
clock = pygame.time.Clock()

block_a = Block(x=500, y=HEIGHT - 50, size=50, speed=0, mass=1, color=RED)
block_b = Block(x=WIDTH-100, y=HEIGHT - 100, size=100,
                speed=-2, mass=100, color=BLUE)

collision_occurred = False
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    WIN.fill(BLACK)

    block_a.check_wall_collision()
    block_b.check_wall_collision()

    if block_a.get_rect().colliderect(block_b.get_rect()):  # check for collision
        block_a.speed, block_b.speed = block_a.get_speed_after_collision(
            block_b), block_b.get_speed_after_collision(block_a)  # update speeds
        # block_a.x, block_b.x = block_b.x-block_a.size, block_a.x + block_a.size

    block_a.update_x_position()
    block_b.update_x_position()

    draw_block(block_a)
    draw_block(block_b)

    pygame.display.flip()
pygame.quit()
