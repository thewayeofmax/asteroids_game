from circleshape import *
from constants import ASTEROID_MIN_RADIUS
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            surface=screen, 
            color="white",
            center=(self.position.x, self.position.y),
            radius=self.radius,
            width= 2
            )
        
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        

        random_angle = random.uniform(20, 50)
        random_velocity_first = self.velocity.rotate(random_angle)
        random_velocity_second = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        first_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        second_asteroid = Asteroid(self.position.x, self.position.y, new_radius)

        first_asteroid.velocity = random_velocity_first * 1.2
        second_asteroid.velocity = random_velocity_second * 1.2


    