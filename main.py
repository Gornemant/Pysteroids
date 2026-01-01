import pygame
from constants import *
from logger import log_state
from circleshape import CircleShape
from player import Player

def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock() #pygame object to track time
	dt = 0
	player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
	while True:
		log_state()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		screen.fill("black")
		player.draw(screen)
		pygame.display.flip()
		dt = clock.tick() / 1000 #returns time passed since last tick in seconds
		clock.tick(MAX_FPS) #limits the maximum FPS to the set constant


if __name__ == "__main__":
    main()
