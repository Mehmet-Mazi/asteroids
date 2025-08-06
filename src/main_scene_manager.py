from state.scene_manager import SceneManager
from game.game_scene import GameScene
from menu.pause_scene import PauseScene


class MainSceneManager(SceneManager):
    def __init__(self, screen, base_scene):
        super().__init__(screen, base_scene)

    def create_transition_mappings(self):
        self._transition_map = {
            "start_game": lambda **kwargs: setattr(
                self, "current_scene", GameScene(self, self._screen, kwargs)
            ),
            "pause": lambda: setattr(
                self, "current_scene", PauseScene(self, self._screen)
            ),
            "resume": lambda: delattr(self, "current_scene"),
            "title_scene": lambda: self.reset_scene(self._base_scene),
        }
