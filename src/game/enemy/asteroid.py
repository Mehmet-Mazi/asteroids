import pygame
import random
from game.helper.circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
  def __init__(self, x, y, radius):
    super().__init__(x, y, radius)

  def split(self):
    self.kill()
    if self.radius <= ASTEROID_MIN_RADIUS:
      return

    new_angle = random.uniform(20,50)
    a1 = self.velocity.rotate(new_angle)
    a2 = self.velocity.rotate(-new_angle)
    new_radius = self.radius - ASTEROID_MIN_RADIUS
    asteroid = Asteroid(self.position.x, self.position.y, new_radius)
    asteroid.velocity = a1 * 1.2
    asteroid = Asteroid(self.position.x, self.position.y, new_radius)
    asteroid.velocity = a2 * 1.2

  def draw(self, screen):
    pygame.draw.circle(screen, "white", self.position, self.radius, 2)
  
  def update(self, dt):
    self.position += self.velocity * dt