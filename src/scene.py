class Scene:
  def __init__(self, scene):
    self.__current_scene = scene
  
  @property
  def current_scene(self):
    return self.__current_scene

  @current_scene.setter
  def current_scene(self, scene):
    self.__current_scene = scene