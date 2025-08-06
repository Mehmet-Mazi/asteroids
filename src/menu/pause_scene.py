import pygame
from state.transition import Transition


class PauseScene:
    allowed_transitions = {"title_scene", "resume"}

    def __init__(self, scene_manager, screen):
        self.scene_manager = scene_manager
        self.screen = screen

    def run(self, events, dt):
        """
        - Add buttons to: Resume, Exit to title screen, Exit Game
        - A nice design (maybe a slightly transparent background so the user can see what state they were in before they paused?)
        """

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return Transition("resume")
