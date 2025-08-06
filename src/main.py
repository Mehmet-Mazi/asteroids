import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from menu.title_scene import TitleScene
from main_scene_manager import MainSceneManager


def main():
    pygame.init()
    print("Starting Asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0
    scene_manager = MainSceneManager(screen, TitleScene)

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
