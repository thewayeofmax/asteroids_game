import pygame
from constants import *
from player import *


def main():
    screen = pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    time_fps = pygame.time.Clock()
    dt = 0

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        player.update(dt)
        screen.fill(color="black")
        player.draw(screen)
        pygame.display.flip()
        dt = time_fps.tick(60) / 1000


if __name__ == "__main__":
    main()