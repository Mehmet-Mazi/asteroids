from scene.scene_manager import SceneManager

class Pause(SceneManager):


  def __init__(self, screen):
    self.screen = screen

  def run(self, dt):
    self.screen.fill("#000000")
    print("paused")