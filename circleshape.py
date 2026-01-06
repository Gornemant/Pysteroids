import pygame

# Base class for game objects provided in Boot.dev course
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # must override
        pass

    def update(self, dt):
        # must override
        pass
    
    #Ch4 L2: Collision handling
    def collides_with(self, other):
        return pygame.math.Vector2.distance_to(self.position, other.position) <= (self.radius + other.radius)
