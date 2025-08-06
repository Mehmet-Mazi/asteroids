import pygame_menu
from state.base_scene import BaseScene
from state.transition import Transition
from constants import SCREEN_HEIGHT, SCREEN_WIDTH


class TitleScene(BaseScene):
    allowed_transitions = {"start_game"}

    def __init__(self, scene_manager, screen):
        self.scene_manager = scene_manager
        self.screen = screen
        self.__pending_transition = None

        self.menu = pygame_menu.Menu(
            "Welcome", SCREEN_WIDTH, SCREEN_HEIGHT, theme=pygame_menu.themes.THEME_BLUE
        )
        self.menu.add.text_input("Name :", default="John Doe")
        self.menu.add.selector(
            "Difficulty :", [("Hard", 1), ("Easy", 2)], onchange=self.set_difficulty
        )
        self.menu.add.button("Play", self.start_the_game)
        self.menu.add.button("Quit", pygame_menu.events.EXIT)

    def set_difficulty(self, value, difficulty):
        pass

    def start_the_game(self):
        self.__pending_transition = Transition("start_game")

    def onclose(self):
        print("closing screen")

    def run(self, events, dt):
        if self.menu.is_enabled():
            self.menu.update(events)
            self.menu.draw(self.screen)

        if self.__pending_transition:
            transition = self.__pending_transition
            self.__pending_transition = None
            return transition
