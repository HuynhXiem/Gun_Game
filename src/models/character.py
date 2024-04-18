import pygame
from .sprite_sheet import sprite_sheet 
jumpIndex = 15
jumpHeight = 15

class Character(pygame.sprite.Sprite):
    enemy = False

    def __init__(self, hp, dame, pos, direct, screen):
        pygame.sprite.Sprite.__init__(self)
        self.hp = hp
        self.max_hp = hp
        self.dame = dame
        self.image = pygame.image.load("res/images/character.png").convert_alpha()
        ratio = self.image.get_rect().width / self.image.get_rect().height
        self.image = pygame.transform.scale(self.image, (50, 50 // ratio)) 
        self.direct = direct
        if direct == -1:
            self.image = pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.isJump = False
        self.jumpCount = jumpIndex
        self.screen = screen

    def update(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy
        self.draw_hp_bar()
        

    def flip(self):
        self.direct *= -1
        self.image = pygame.transform.flip(self.image, True, False)

    def jump(self):
        if self.isJump:
            if self.jumpCount >= -jumpIndex - 1:
                neg = 1
                if self.jumpCount < 0:
                    neg = -1
                self.rect.y -= jumpHeight * neg
                self.jumpCount -= 1
            else:
                self.isJump = False
                self.jumpCount = jumpIndex

    def draw_hp_bar(self):
        hp_bar_width = self.rect.width
        hp_bar_height = 5
        hp_ratio = self.hp / self.max_hp
        hp_bar_length = int(hp_bar_width * hp_ratio)
        hp_bar_color = (0, 255, 0)  # Màu xanh lá cây

        pygame.draw.rect(self.screen, (255, 0, 0), [self.rect.x, self.rect.y - hp_bar_height - 5, hp_bar_width, hp_bar_height])
        pygame.draw.rect(self.screen, hp_bar_color, [self.rect.x, self.rect.y - hp_bar_height - 5, hp_bar_length, hp_bar_height])

