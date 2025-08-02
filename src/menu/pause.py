import pygame

class Pause:

  def __init__(self, scene_manager, screen):
    self.scene_manager = scene_manager
    self.screen = screen

  def run(self, events, dt):
    self.screen.fill("#000000")
    for event in events:
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          del self.scene_manager.current_scene
 

    