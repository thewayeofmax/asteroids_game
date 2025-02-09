import pygame

class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius
    
    #methods to be overriden by child classes
    def draw(self, screen):
        pass

    def update(self, dt):
        pass

    def collision(self, other):
        distance = self.position.distance_to(other.position)
        both_radius_distance = self.radius + other.radius
        
        if distance <= both_radius_distance:
            return True
        return False