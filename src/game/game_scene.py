import pygame
import sys
from game.player.base_player import BasePlayer
from game.weapon.basic_bullet import BasicBullet
from game.enemy.asteroid import Asteroid
from game.enemy.asteroidfield import AsteroidField
from menu.pause import Pause
from constants import *

class GameScene:
  
  def __init__(self, scene_manager, screen):
    self.scene_manager = scene_manager
    self.screen = screen
    
    self.asteroids = pygame.sprite.Group() 
    self.updatable = pygame.sprite.Group()
    self.drawable = pygame.sprite.Group()
    self.bullets = pygame.sprite.Group()

    # look into factory method
    BasePlayer.containers = (self.updatable, self.drawable)
    Asteroid.containers = (self.asteroids, self.updatable, self.drawable)
    AsteroidField.containers = (self.updatable)
    BasicBullet.containers = (self.bullets, self.updatable, self.drawable)

    self.player = BasePlayer(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    self.asteroidSpawner = AsteroidField()

  def run(self, events, dt):
    for event in events:
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          self.scene_manager.current_scene = Pause(self.scene_manager, self.screen)
 
    self.updatable.update(dt)

    for obj in self.asteroids:
        if obj.collision(self.player):
            print("Game over!")
            sys.exit(0) # TODO call game over instead!
        
        for bullet in self.bullets:
            if obj.collision(bullet):
                obj.split()
                bullet.kill()
        
    for sprite in self.drawable:
        sprite.draw(self.screen)