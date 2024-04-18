import pygame
import sys

# Khai báo một số màu cơ bản
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class bullet(pygame.sprite.Sprite):
    def __init__(self, gun, pos, damage):
        super().__init__()
        self.image = pygame.Surface((10, 5))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect(center=pos)
        self.speed = 10  # Tốc độ di chuyển của đạn
        self.gun = gun
        self.direct = gun.direct
        self.damage = damage  # Sát thương của đạn

    def update(self):
        self.rect.x += self.direct * self.speed
        if (self.rect.x > 1000):
            self.die()
    def die(self):
        self.gun.bullets.remove(self)
        self.kill()