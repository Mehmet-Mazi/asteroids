class SceneManager:
  def __init__(self):
    self.stack = []
  
  def next_scene(self, scene):
    self.stack.append(scene)
    
  def prev_scene(self):
    return self.stack.pop()
    
  def current_scene(self):
    return self.stack[-1]