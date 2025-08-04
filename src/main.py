import pygame
import sys
from constants import *
from menu.title_scene import TitleScene
from game.game_scene import GameScene
from state.scene_manager import SceneManager

def main():
    pygame.init()
    print("Starting Asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)
    
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    
    clock = pygame.time.Clock()
    dt = 0
    scene_manager = SceneManager(screen)
    scene_manager.current_scene = TitleScene(scene_manager, screen) # Starting scene explicitly set
    # scene_manager.current_scene = GameScene(scene_manager, screen) # Starting scene
    
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                return

        scene_manager.update(events, dt)

        print(scene_manager.stack())
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__": 
    main()

