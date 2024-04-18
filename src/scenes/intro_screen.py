import pygame

class IntroScreen:
    def __init__(self, DISPLAYSURF, intro_screen, button_rect, button_hover, font):
        self.DISPLAYSURF = DISPLAYSURF
        self.intro_screen = intro_screen
        self.button_rect = button_rect
        self.button_hover = button_hover
        self.font = font

        self.back_button_rect = pygame.Rect(50, 550, 200, 50)
        self.start_game_button_rect = pygame.Rect(650, 550, 200, 50)
        self.choice1_game_button_rect = pygame.Rect(200, 350, 200, 50)
        self.choice2_game_button_rect = pygame.Rect(500, 350, 200, 50)

    def show_intro_screen(self):
        self.DISPLAYSURF.blit(self.intro_screen, (0, 0))

        # Kiểm tra nếu chuột nằm trong phạm vi của button_rect thì cập nhật button_hover
        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.button_hover = self.button_rect.collidepoint(mouse_x, mouse_y)

        if self.button_hover:
            pygame.draw.rect(self.DISPLAYSURF, (128, 128, 128), self.button_rect, border_radius=10)
        else:
            pygame.draw.rect(self.DISPLAYSURF, (255, 255, 255), self.button_rect, border_radius=8, width=2)

        text = self.font.render('PLAY GAME', True, (255, 255, 255))
        text_rect = text.get_rect(center=self.button_rect.center)
        self.DISPLAYSURF.blit(text, text_rect.topleft)

        pygame.display.set_caption('Shooter Battle')
