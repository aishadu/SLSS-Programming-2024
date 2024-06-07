
import pygame as pg
import random

# Constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
WIDTH = 1280
HEIGHT = 720
SCREEN_SIZE = (WIDTH, HEIGHT)

def start():
    """Environment Setup and Game Loop"""
    pg.init()

    # Game State Variables
    screen = pg.display.set_mode(SCREEN_SIZE)
    done = False
    clock = pg.time.Clock()

    # Player
    player_rect = pg.Rect(WIDTH // 2 - 25, HEIGHT - 50, 50, 10)
    player_speed = 10

    # Enemy
    enemy_rect = pg.Rect(random.randint(0, WIDTH - 50), 50, 50, 10)
    enemy_speed = 15

    # Game Over Flag
    game_over = False

    # Main Loop
    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True

        if not game_over:
            # Player Controls
            keys = pg.key.get_pressed()
            if keys[pg.K_LEFT]:
                player_rect.x -= player_speed
            if keys[pg.K_RIGHT]:
                player_rect.x += player_speed

            # Move the enemy
            enemy_rect.y += enemy_speed
            if enemy_rect.y > HEIGHT:
                enemy_rect.y = 0
                enemy_rect.x = random.randint(0, WIDTH - 50)

            # Collision detection
            if player_rect.colliderect(enemy_rect):
                game_over = True

        # Draw items
        screen.fill(BLACK)
        pg.draw.rect(screen, WHITE, player_rect)
        pg.draw.rect(screen, RED, enemy_rect)

        # Display "Game Over" message
        if game_over:
            font = pg.font.Font(None, 36)
            text = font.render("Game Over!", True, WHITE)
            screen.blit(text, (WIDTH // 2 - 70, HEIGHT // 2))

        # Update the screen
        pg.display.flip()

        # Tick the Clock
        clock.tick(60)  # 60 fps

    pg.quit()


def main():
    start()

if __name__ == "__main__":
    main()
