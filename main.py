import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *


def main():
    screen = pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    time_fps = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updatable.update(dt)
        for asteroid in asteroids:
            asteroid.collision(player)

        screen.fill(color="black")
        
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
        dt = time_fps.tick(60) / 1000


if __name__ == "__main__":
    main()