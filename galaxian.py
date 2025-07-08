import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 480, 640
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Galaxian Clone")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Player
player_width, player_height = 40, 20
player = pygame.Rect(WIDTH // 2 - player_width // 2, HEIGHT - 60, player_width, player_height)
player_speed = 5

# Bullet
bullet = None
bullet_speed = -7

# Enemies
enemy_rows = 5
enemy_cols = 8
enemy_width, enemy_height = 30, 20
enemy_gap = 10
enemy_speed = 1
enemies = []
for row in range(enemy_rows):
    for col in range(enemy_cols):
        x = 50 + col * (enemy_width + enemy_gap)
        y = 50 + row * (enemy_height + enemy_gap)
        enemies.append(pygame.Rect(x, y, enemy_width, enemy_height))

def draw():
    screen.fill(BLACK)
    pygame.draw.rect(screen, GREEN, player)
    if bullet:
        pygame.draw.rect(screen, WHITE, bullet)
    for e in enemies:
        pygame.draw.rect(screen, RED, e)
    pygame.display.flip()

def handle_input():
    global bullet
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.left > 0:
        player.move_ip(-player_speed, 0)
    if keys[pygame.K_RIGHT] and player.right < WIDTH:
        player.move_ip(player_speed, 0)
    if keys[pygame.K_SPACE] and bullet is None:
        bullet = pygame.Rect(player.centerx - 2, player.top - 10, 4, 10)

def update_bullet():
    global bullet
    if bullet:
        bullet.move_ip(0, bullet_speed)
        if bullet.bottom < 0:
            bullet = None
        else:
            for e in enemies:
                if bullet.colliderect(e):
                    enemies.remove(e)
                    bullet = None
                    break

def update_enemies():
    global enemy_speed
    move_down = False
    for e in enemies:
        e.x += enemy_speed
        if e.right >= WIDTH or e.left <= 0:
            move_down = True
    if move_down:
        enemy_speed *= -1
        for e in enemies:
            e.y += enemy_height

clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    handle_input()
    update_bullet()
    update_enemies()
    draw()
    if any(e.bottom >= player.top for e in enemies):
        running = False
    clock.tick(60)

pygame.quit()
