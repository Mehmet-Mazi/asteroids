import pygame
import sys
from constants import *
from game.game_scene import GameScene
from menu.pause import Pause
from scene.scene_manager import SceneManager

def main():
    pygame.init()
    print("Starting Asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)
    
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    
    clock = pygame.time.Clock()
    dt = 0
    scene_manager = SceneManager()
    scene_manager.next_scene(GameScene(scene_manager, screen)) # Starting scene
    print("first stack", scene_manager.stack)
    
    
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                return

        screen.fill("#3c3330")

        scene_manager.current_scene().run(events, dt)
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__": 
    main()

