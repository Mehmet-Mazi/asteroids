class SceneManager:
  def __init__(self):
    self.__stack = []
    # self.__current_stack = self.stack[-1]

  @property
  def current_scene(self):
    return self.__stack[-1]
  
  @current_scene.setter
  def current_scene(self, scene):
    self.__stack.append(scene)

  @current_scene.deleter
  def current_scene(self):
    return self.__stack.pop()
    