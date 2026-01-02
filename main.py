import pygame
from constants import *
from logger import log_state
from circleshape import CircleShape
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock() #pygame object to track time
	dt = 0
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = updatable
	player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
	asteroid_field = AsteroidField()
	
	while True:
		log_state()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		screen.fill("black")
		updatable.update(dt)
		for i in drawable:
			i.draw(screen)
		pygame.display.flip()
		dt = clock.tick(MAX_FPS) / 1000 #returns time passed since last tick in seconds, MAX_FPS limits the maximum FPS to the set constant


if __name__ == "__main__":
    main()
