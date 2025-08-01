class SceneManager:
  stack = []

  
  def next_scene(self, scene):
    self.stack.append(scene)
    
  def current_scene(self, dt):
    return self.stack[-1].run(dt)
  
  def run(self):
    pass