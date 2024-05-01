import pygame as pg
import random
# --CONSTANTS--
# COLOURS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
EMERALD = (21, 219, 147)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)
WIDTH = 1280  # Pixels
HEIGHT = 720
SCREEN_SIZE = (WIDTH, HEIGHT)
class Snowflake(pg.sprite.Sprite):
    def __init__(self, size: int):
        """
        Params:
            size: diameter of the snowflake in pixels
        """
        #super class constructor
        super().__init__()
        # create a blank surface
        self.image = pg.Surface((size, size)) # width and height
        # and draw a circle inside of it
        pg.draw.circle(self.image, WHITE, (size // 2, size //2),  size // 2)
        self.rect = self.image.get_rect()
        #spawn it in the middle of the screen
        # self.rect.centerx = WIDTH // 2
        # self.rect.centery = HEIGHT // 2
        self.rect.x = random.randrange(0, WIDTH)
        self.rect.y = random.randrange(0, HEIGHT)
        self.vel_y = -2
    def update(self):
        self.rect.y -= self.vel_y
        # If it falls off the bottom, "TELEPORT IT" up to the top
        if self.rect.bottom >= HEIGHT + 10:
            self.rect.y = -10
            self.rect.x = self.rect.x
def start():
    """Environment Setup and Game Loop"""
    pg.init()
    # --Game State Variables--
    screen = pg.display.set_mode(SCREEN_SIZE)
    done = False
    clock = pg.time.Clock()
    # All sprites go in this sprite Group
    all_sprites = pg.sprite.Group()
    # add one snowflake to the all_sprites group
    for _ in range(100):
        all_sprites.add(Snowflake(10))
    pg.display.set_caption("Snowfall Landscape")
    # --Main Loop--
    while not done:
        # --- Event Listener
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
        # --- Update the world state
        # update the state of all sprites
        all_sprites.update()
        # --- Draw items
        screen.fill(BLACK)
        # draw all the sprites
        all_sprites.draw(screen)
        # Update the screen with anything new
        pg.display.flip()
        # --- Tick the Clock
        clock.tick(60)  # 60 fps
def main():
    start()
if __name__ == "__main__":
    main()