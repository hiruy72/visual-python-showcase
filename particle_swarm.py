import pygame
import random
import math

# Initialize
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Particle Swarm Visualizer")
clock = pygame.time.Clock()

# Particle class
class Particle:
    def __init__(self):
        self.x = random.uniform(0, WIDTH)
        self.y = random.uniform(0, HEIGHT)
        self.size = random.uniform(2, 4)
        self.speed = random.uniform(1, 3)
        self.angle = random.uniform(0, 2 * math.pi)
        self.color = (255, 255, 255)

    def move(self, target_x, target_y):
        dx = target_x - self.x
        dy = target_y - self.y
        angle_to_mouse = math.atan2(dy, dx)
        self.angle += (angle_to_mouse - self.angle) * 0.05
        self.x += math.cos(self.angle) * self.speed
        self.y += math.sin(self.angle) * self.speed

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), int(self.size))

particles = [Particle() for _ in range(150)]

# Main loop
running = True
while running:
    screen.fill((10, 10, 30))
    mouse_x, mouse_y = pygame.mouse.get_pos()

    for particle in particles:
        particle.move(mouse_x, mouse_y)
        particle.draw(screen)

    pygame.display.flip()
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
