import pygame


class SelectScreen:
    def __init__(self, DISPLAYSURF, select_screen, font, back_button_rect, back_button_hover,
                 start_game_button_rect, start_game_button_hover, pve_selected,
                 choice1_game_button_rect, choice1_game_button_hover, pvp_selected,
                 choice2_game_button_rect, choice2_game_button_hover):
        self.DISPLAYSURF = DISPLAYSURF
        self.select_screen = select_screen
        self.font = font
        self.back_button_rect = back_button_rect
        self.back_button_hover = back_button_hover
        self.start_game_button_rect = start_game_button_rect
        self.start_game_button_hover = start_game_button_hover
        self.pve_selected = pve_selected
        self.choice1_game_button_rect = choice1_game_button_rect
        self.choice1_game_button_hover = choice1_game_button_hover
        self.pvp_selected = pvp_selected
        self.choice2_game_button_rect = choice2_game_button_rect
        self.choice2_game_button_hover = choice2_game_button_hover

    def show_select_screen(self, model):
        self.DISPLAYSURF.blit(self.select_screen, (0, 0))

        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Kiểm tra hover cho nút BACK
        back_button_hover = self.back_button_rect.collidepoint(mouse_x, mouse_y)
        if back_button_hover:
            pygame.draw.rect(self.DISPLAYSURF, (128, 128, 128), self.back_button_rect, border_radius=10)
        else:
            pygame.draw.rect(self.DISPLAYSURF, (255, 255, 255), self.back_button_rect, border_radius=8, width=2)

        text = self.font.render('BACK', True, (255, 255, 255))
        text_rect = text.get_rect(center=self.back_button_rect.center)
        self.DISPLAYSURF.blit(text, text_rect.topleft)

        # Kiểm tra hover cho nút START
        start_game_button_hover = self.start_game_button_rect.collidepoint(mouse_x, mouse_y)
        if start_game_button_hover:
            pygame.draw.rect(self.DISPLAYSURF, (128, 128, 128), self.start_game_button_rect, border_radius=10)
        else:
            pygame.draw.rect(self.DISPLAYSURF, (255, 255, 255), self.start_game_button_rect, border_radius=8, width=2)

        text = self.font.render('START', True, (255, 255, 255))
        text_rect = text.get_rect(center=self.start_game_button_rect.center)
        self.DISPLAYSURF.blit(text, text_rect.topleft)

        # Kiểm tra hover cho nút PvE
        choice1_game_button_hover = self.choice1_game_button_rect.collidepoint(mouse_x, mouse_y)
        if not model.pve_selected:
            if choice1_game_button_hover:
                pygame.draw.rect(self.DISPLAYSURF, (128, 128, 128), self.choice1_game_button_rect, border_radius=10)
            else:
                pygame.draw.rect(self.DISPLAYSURF, (255, 255, 255), self.choice1_game_button_rect, border_radius=8, width=2)
        else:
            pygame.draw.rect(self.DISPLAYSURF, (192, 192, 192), self.choice1_game_button_rect, border_radius=8)
        # if self.pve_selected:
        #     pygame.draw.rect(self.DISPLAYSURF, (192, 192, 192), self.choice1_game_button_rect, border_radius=8)

        text = self.font.render('PvE', True, (255, 255, 255))
        text_rect = text.get_rect(center=self.choice1_game_button_rect.center)
        self.DISPLAYSURF.blit(text, text_rect.topleft)

        # Kiểm tra hover cho nút PvP
        if not model.pvp_selected:
            choice2_game_button_hover = self.choice2_game_button_rect.collidepoint(mouse_x, mouse_y)
            if choice2_game_button_hover:
                pygame.draw.rect(self.DISPLAYSURF, (128, 128, 128), self.choice2_game_button_rect, border_radius=10)
            else:
                pygame.draw.rect(self.DISPLAYSURF, (255, 255, 255), self.choice2_game_button_rect, border_radius=8, width=2)
        else:
            pygame.draw.rect(self.DISPLAYSURF, (192, 192, 192), self.choice2_game_button_rect, border_radius=8)
        # if self.pvp_selected:
        #     pygame.draw.rect(self.DISPLAYSURF, (192, 192, 192), self.choice2_game_button_rect, border_radius=8)

        text = self.font.render('PvP', True, (255, 255, 255))
        text_rect = text.get_rect(center=self.choice2_game_button_rect.center)
        self.DISPLAYSURF.blit(text, text_rect.topleft)

        pygame.display.set_caption('Select menu')
