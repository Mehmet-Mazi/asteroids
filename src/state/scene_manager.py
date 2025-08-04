from state.transition import Transition
from game.game_scene import GameScene
from menu.pause_scene import PauseScene
from menu.title_scene import TitleScene

class SceneManager:
  def __init__(self, screen, base_scene):
    self.__screen = screen
    self.__base_scene = base_scene(self, self.__screen)
    self.__stack = [self.__base_scene]
    self.__transition_map = {
      "start_game": lambda **kwargs:setattr(self, "current_scene", GameScene(self, self.__screen, kwargs)),
      "pause": lambda:setattr(self, "current_scene", PauseScene(self, self.__screen)),
      "resume": lambda:delattr(self, "current_scene"),
      "title_scene": lambda: self.reset_scene(self.__base_scene),
    }

  @property
  def current_scene(self):
    return self.__stack[-1]
  
  @current_scene.setter
  def current_scene(self, scene):
    self.__stack.append(scene)

  @current_scene.deleter
  def current_scene(self):
    return self.__stack.pop()

  def stack(self):
    return self.__stack
    
  def clear(self):
    self.__stack = []

  def reset_scene(self, transition):
    self.clear()
    self.current_scene = transition

  def update(self, events, dt):
    result = self.current_scene.run(events, dt)
    if isinstance(result, Transition):
      print("result", result)
      self.handle_transition(result)

  def handle_transition(self, transition):
    allowed = getattr(self.current_scene, "allowed_transitions", set())

    if transition.type not in allowed:
      raise Exception(f"Invalid transition '{transition.type}' from {type(self.current_scene).__name__}")

    self.__transition_map[transition.type](**transition.data)