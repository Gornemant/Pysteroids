import pygame
import random
from logger import log_state, log_event
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x ,y , radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    
    def update(self, dt):
        self.position += (self.velocity * dt)
    
    #handles destroyed asteroid removal and splitting if applicable
    def split(self, asteroid_field):
        log_event("asteroid_shot")
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            log_event("asteroid_kill")
            return
        log_event("asteroid_split")
        new_angle = random.uniform(20, 50)
        new_velocity_1 = self.velocity.rotate(new_angle)
        new_velocity_2 = self.velocity.rotate(-new_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_field.spawn(new_radius, self.position, new_velocity_1 * 1.2)
        asteroid_field.spawn(new_radius, self.position, new_velocity_2 * 1.2)
