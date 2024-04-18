import pygame


class LoseScreen:
    def __init__(self, DISPLAYSURF, lose_screen, font, replay_button_rect, replay_button_hover,
                 home_game_button_rect, home_game_button_hover, model):
        self.DISPLAYSURF = DISPLAYSURF
        self.lose_screen = lose_screen
        self.font = font
        self.replay_button_rect = replay_button_rect
        self.replay_button_hover = replay_button_hover
        self.home_game_button_rect = home_game_button_rect
        self.home_game_button_hover = home_game_button_hover
        self.model = model

    def show_lose_screen(self):
        self.DISPLAYSURF.blit(self.lose_screen, (0, 0))

        # Kiểm tra nếu chuột nằm trong phạm vi của button_rect thì cập nhật button_hover
        mouse_x, mouse_y = pygame.mouse.get_pos()

        self.replay_button_hover = self.replay_button_rect.collidepoint(mouse_x, mouse_y)
        if self.replay_button_hover:
            pygame.draw.rect(self.DISPLAYSURF, (128, 128, 128), self.replay_button_rect, border_radius=10)
        else:
            pygame.draw.rect(self.DISPLAYSURF, (255, 255, 255), self.replay_button_rect, border_radius=8, width=2)

        text = self.font.render('REPLAY', True, (255, 255, 255))
        text_rect = text.get_rect(center=self.replay_button_rect.center)
        self.DISPLAYSURF.blit(text, text_rect.topleft)

        self.home_game_button_hover = self.home_game_button_rect.collidepoint(mouse_x, mouse_y)
        if self.home_game_button_hover:
            pygame.draw.rect(self.DISPLAYSURF, (128, 128, 128), self.home_game_button_rect, border_radius=10)
        else:
            pygame.draw.rect(self.DISPLAYSURF, (255, 255, 255), self.home_game_button_rect, border_radius=8, width=2)

        text = self.font.render('HOME', True, (255, 255, 255))
        text_rect = text.get_rect(center=self.home_game_button_rect.center)
        self.DISPLAYSURF.blit(text, text_rect.topleft)

        pygame.display.set_caption('Shooter Battle')
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.replay_button_rect.collidepoint(event.pos[0], event.pos[1]):
                    self.model.current_screen = "pve"
                elif self.home_game_button_rect.collidepoint(event.pos[0], event.pos[1]):
                    self.model.current_screen = "intro"
