import pygame
import sys

from pygame import QUIT

from .models.game_model import GameModel
from .scenes.intro_screen import IntroScreen
from .scenes.select_screen import SelectScreen
from .scenes.pve_scene import PVE
from .scenes.win_screen import WinScreen
from .scenes.lose_screen import LoseScreen
from .controllers.controller import GameController


def main():
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((900, 700))

    intro_screen_image = pygame.image.load('res/images/introScreen.png')
    intro_screen_button_rect = pygame.Rect(350, 588, 200, 50)
    game_screen_image = pygame.image.load('res/images/select.png')
    font = pygame.font.Font('res/fonts/VT323-Regular.ttf', 50)
    win_screen = pygame.image.load('res/images/win.png')
    lose_screen = pygame.image.load('res/images/lose.png')

    button_hover = False  # Set button_hover to False initially

    # Khởi tạo Model, View, Controller
    game_model = GameModel()
    intro_view = IntroScreen(DISPLAYSURF, intro_screen_image, intro_screen_button_rect, button_hover, font)

    back_button_rect = pygame.Rect(50, 550, 200, 50)
    start_game_button_rect = pygame.Rect(650, 550, 200, 50)
    choice1_game_button_rect = pygame.Rect(200, 350, 200, 50)
    choice2_game_button_rect = pygame.Rect(500, 350, 200, 50)

    start_button_clicked = False
    pve_selected = False
    pvp_selected = False

    select_view = SelectScreen(DISPLAYSURF, game_screen_image, font, back_button_rect, button_hover,
                               start_game_button_rect, button_hover, pve_selected,
                               choice1_game_button_rect, button_hover, pvp_selected,
                               choice2_game_button_rect, button_hover)

    game_controller = GameController(game_model, intro_view)

    replay_button_rect = pygame.Rect(200, 350, 200, 50)
    home_game_button_rect = pygame.Rect(500, 350, 200, 50)

    # stt_view = LoseScreen(DISPLAYSURF, lose_screen, font, replay_button_rect, button_hover,home_game_button_rect, button_hover)

    while True:
        # Xử lý sự kiện
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            game_controller.handle_events(event)

        # Cập nhật giao diện người dùng
        if game_model.current_screen == 'intro':
            intro_view.show_intro_screen()
        elif game_model.current_screen == 'select':
            select_view.show_select_screen(game_model)
        elif game_model.current_screen == 'pve':
            # Bên trong hàm main()
            pve_scene = PVE(DISPLAYSURF, game_model) # Khởi tạo màn hình trò chơi PvE
            # pve_scene.run_pve()  # Chạy màn hình trò chơi PvE
        elif game_model.current_screen == 'win':
            win_Screen = WinScreen(DISPLAYSURF, win_screen, font, replay_button_rect, button_hover,home_game_button_rect, button_hover, game_model)
            win_Screen.show_win_screen()
        elif game_model.current_screen == 'lose':
            lose_Screen = LoseScreen(DISPLAYSURF, lose_screen, font, replay_button_rect, button_hover,home_game_button_rect, button_hover, game_model)
            lose_Screen.show_lose_screen()
        pygame.display.update()


if __name__ == "__main__":
    main()
