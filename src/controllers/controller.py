import pygame
from pygame import MOUSEBUTTONDOWN

class GameController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def handle_events(self, event):
        if event.type == MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            if self.model.current_screen == 'intro':
                if self.view.button_rect.collidepoint(mouse_x, mouse_y):
                    self.model.current_screen = 'select'
            elif self.model.current_screen == 'select':
                if self.view.back_button_rect.collidepoint(mouse_x, mouse_y):
                    self.model.current_screen = 'intro'
                elif self.view.choice1_game_button_rect.collidepoint(mouse_x, mouse_y):
                    self.model.select_pve()
                elif self.view.choice2_game_button_rect.collidepoint(mouse_x, mouse_y):
                    self.model.select_pvp()
                elif self.view.start_game_button_rect.collidepoint(mouse_x, mouse_y):
                    self.model.click_start_button()
                    if self.model.pve_selected and self.model.start_button_clicked:
                        self.model.current_screen = 'pve'
                        # Kiểm tra trạng thái của nhân vật và chuyển màn hình nếu cần
                        if not self.model.character_alive:
                            self.model.current_screen = 'lose'  # Chuyển sang màn hình thua
                    else:
                        self.model.current_screen = 'pvp'
                        # Kiểm tra trạng thái của nhân vật và chuyển màn hình nếu cần
                        if not self.model.character_alive:
                            self.model.current_screen = 'lose'  # Chuyển sang màn hình thua

