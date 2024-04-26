import pygame
from .bullet import bullet 
class Gun(pygame.sprite.Sprite):
    # bullets = pygame.sprite.Group()
    max_bull = 3
    

    def __init__(self, character, level):
        super().__init__()
        self.image = pygame.image.load("res/images/gun.png").convert_alpha()
        ratio = self.image.get_rect().width / self.image.get_rect().height
        self.image = pygame.transform.scale(self.image, (100, 100 / ratio)) 
        self.rect = self.image.get_rect()
        self.character = character
        self.level = level
        self.damage = level
        self.direct = character.direct
        self.bullets = []
        self.current_bull = 0
        self.shoot_sound = pygame.mixer.Sound("res/sounds/shoot.mp3")
        if self.direct == -1:
            self.image = pygame.transform.flip(self.image, True, False)
        self.update()

    def shoot(self):
        if self.current_bull < self.max_bull:
            # print(self.character.player , ": ", self.current_bull)
            _bullet = bullet(self, (self.rect.midright[0] - 20, self.rect.midright[1] - 10),self.damage)
            self.shoot_sound.play()
            self.bullets.append(_bullet)
            self.current_bull += 1
            return _bullet
        return False

    def flip(self):
        self.direct *= -1
        self.image = pygame.transform.flip(self.image, True, False)
        
    def update(self):
        if not self.character.alive():
            self.kill()
        if (self.character.direct != self.direct):
            self.flip()
        self.rect.centerx = self.character.rect.centerx + 20 * self.direct
        self.rect.centery = self.character.rect.centery + 20

        for bull in self.bullets:
            bull.update()
