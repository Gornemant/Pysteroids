import pygame
from constants import PLAYER_RADIUS, LINE_WIDTH, PLAYER_TURN_SPEED, PLAYER_SPEED
from circleshape import CircleShape


class Player(CircleShape):
	def __init__(self, x, y):
		super().__init__(x,y,PLAYER_RADIUS)
		self.rotation = 0
		#Keybindings added beyond scope for easier custom keybinds at later point
		self.keybind_up = pygame.K_UP
		self.keybind_down = pygame.K_DOWN
		self.keybind_left = pygame.K_LEFT
		self.keybind_right = pygame.K_RIGHT
	
	# triangle method provided by Boot.dev in the course
	def triangle(self):
		forward = pygame.Vector2(0, 1).rotate(self.rotation)
		right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
		a = self.position + forward * self.radius
		b = self.position - forward * self.radius - right
		c = self.position - forward * self.radius + right
		return [a, b, c]
	
	def draw(self, screen):
		pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)
	
	def rotate(self, dt):
		self.rotation += PLAYER_TURN_SPEED * dt
	
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
    
	def move(self, dt):
		#Unit vector code provided in Boot.dev lesson
		unit_vector = pygame.Vector2(0, 1)
		rotated_vector = unit_vector.rotate(self.rotation)
		rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
		self.position += rotated_with_speed_vector