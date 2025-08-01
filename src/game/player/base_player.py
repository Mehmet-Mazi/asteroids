import pygame
from game.helper.circleshape import CircleShape
from game.weapon.basic_bullet import BasicBullet
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, SHOT_RADIUS, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN

class BasePlayer(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.current_speed = 0
        self.shoot_cooldown = 0

    def triangle(self):
        forward = pygame.Vector2(0,1).rotate(self.rotation)
        right = pygame.Vector2(0,1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a,b,c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def set_direction(self, forward, dt):
        if forward and self.current_speed < 0:
            self.decelerate(dt)
        elif not forward and self.current_speed > 0:
            self.decelerate(dt)
        else:
            self.current_speed = PLAYER_SPEED if forward else -PLAYER_SPEED

    def decelerate(self, dt):
        DECELERATION = 300
        if self.current_speed > 0:
            self.current_speed = max(self.current_speed - DECELERATION * dt, 0)
        elif self.current_speed < 0:
            self.current_speed = min(self.current_speed + DECELERATION * dt, 0)

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * self.current_speed * dt # Example of what is happening -> player.position(200, 400) + next_position_per_frame((-0.12, 1.88) * 10 * 0.16)

    def update(self, dt):
        self.shoot_cooldown -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)

        if keys[pygame.K_w]:
            self.set_direction(True, dt)
        elif keys[pygame.K_s]:
            self.set_direction(False, dt)
        else:
            self.decelerate(dt)

        if keys[pygame.K_SPACE]:
            self.shoot(dt)

        self.move(dt)

    def shoot(self, dt):
        if self.shoot_cooldown > 0:
            return
        self.shoot_cooldown = PLAYER_SHOOT_COOLDOWN
        bullet = BasicBullet(self.position.x, self.position.y, SHOT_RADIUS)
        bullet.velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
