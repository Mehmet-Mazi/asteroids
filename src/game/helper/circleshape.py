import pygame

class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x,y)
        self.velocity = pygame.Vector2(0,0)
        self.radius = radius

    def collision(self, target):
        distance = self.position.distance_to(target.position)
        if distance <= (self.radius + target.radius):
            return True
        else:
            return False

    def draw(self, screen):
        pass

    def update(self, dt):
        pass

