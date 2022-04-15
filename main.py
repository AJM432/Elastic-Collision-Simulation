import pygame

pygame.init()
WIDTH = 1000
HEIGHT = 500
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Collision Simulation")
clock = pygame.time.Clock()


class Block:
    def __init__(self, x, y, size, speed, mass, color):
        self.x = x
        self.y = y
        self.size = size
        self.speed = speed
        self.mass = mass
        self.color = color

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.size, self.size)

    def draw(self):
        pygame.draw.rect(WIN, self.color, self.get_rect())

    def update_x_position(self):
        self.x += self.speed
        # self.speed = self.speed -  self.speed/(abs(self.speed))*0.01 # friction

    def get_speed_after_collision(self, object_2): # from elastic collision formula
        return ((self.mass-object_2.mass)/(self.mass + object_2.mass))*self.speed + \
            ((2*object_2.mass)/(self.mass + object_2.mass))*object_2.speed

    def check_wall_collision(self):
        if self.x <= 0:
            self.x = 0
            self.speed *= -1
        elif self.x + self.size >= WIDTH:
            self.x = WIDTH - self.size
            self.speed *= -1
        

block_a = Block(x=500, y=HEIGHT - 50, size=50, speed=0, mass=1, color=RED)
block_b = Block(x=WIDTH-100, y=HEIGHT - 100, size=100, speed=-2, mass=100, color=BLUE)


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


    if block_a.get_rect().colliderect(block_b.get_rect()): # check for collision
        block_a.speed, block_b.speed = block_a.get_speed_after_collision(block_b), block_b.get_speed_after_collision(block_a) # update speeds
        # block_a.x, block_b.x = block_b.x-block_a.size, block_a.x + block_a.size
        
    block_a.update_x_position()
    block_b.update_x_position()

    block_a.draw()
    block_b.draw()

    pygame.display.flip()
pygame.quit()
