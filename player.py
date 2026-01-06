import pygame
from constants import *
from circleshape import CircleShape
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation = 0
        self.shot_cooldown_timer = 0
        #Keybindings added beyond scope for easier custom keybinds at later point
        self.keybind_up = pygame.K_UP
        self.keybind_down = pygame.K_DOWN
        self.keybind_left = pygame.K_LEFT
        self.keybind_right = pygame.K_RIGHT
        self.keybind_shoot = pygame.K_SPACE
    
    # triangle method provided by Boot.dev in the course
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    #draw player ship
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)
    
    #rotates the ship in relation to turn speed and time since last tick
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    #updates the sjip according to what keys are pressed, simultaneous opposite directions are ignored instead of cancelling each other out
    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[self.keybind_left] and not keys[self.keybind_right]:
            self.rotate(-dt)
        if keys[self.keybind_right] and not keys[self.keybind_left]:
            self.rotate(dt)
        if keys[self.keybind_up] and not keys[self.keybind_down]:
            self.move(dt)
        if keys[self.keybind_down] and not keys[self.keybind_up]:
            self.move(-dt)
        #cooldown timer between shots
        if self.shot_cooldown_timer > 0:
            self.shot_cooldown_timer -= dt
        else:
            #ship forward/backwards velocity impacts shot speed, considered alternative was to handle it through ship velocity variable
            #but would require a velocity update every tick or when movement key is released which is not yet required.
            if keys[self.keybind_shoot] and keys[self.keybind_up] and not keys[self.keybind_down]:
                self.shoot(1)
            if keys[self.keybind_shoot] and keys[self.keybind_down] and not keys[self.keybind_up]:
                self.shoot(-1)
            if keys[self.keybind_shoot] and not (keys[self.keybind_up] or keys[self.keybind_down]):
                self.shoot(0)
    
    def move(self, dt):
        #Unit vector code provided in Boot.dev course
        #unit_vector = pygame.Vector2(0, 1)
        #rotated_vector = unit_vector.rotate(self.rotation)
        #rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        #self.position += rotated_with_speed_vector
        #This basically does the same in one line
        self.position += pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SPEED * dt
    
    #Ch4 L3: Shooting, direction input beyond scope for ship speed to impact shot velocity.
    def shoot(self, direction):
        ship_front = self.triangle()[0]
        shot = Shot(*ship_front)
        rotated_vector = pygame.Vector2(0, 1).rotate(self.rotation)
        shot.velocity = rotated_vector * (PLAYER_SHOOT_SPEED + direction * PLAYER_SPEED)
        self.shot_cooldown_timer = PLAYER_SHOOT_COOLDOWN_SECONDS
    