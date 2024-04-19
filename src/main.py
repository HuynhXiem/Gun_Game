import pygame
import sys
from pygame.locals import *

from scenes.game_scene import GameScene

def main():
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((900, 700))
    intro_screen = pygame.image.load('src/scenes/introScreen.png')
    game_screen = pygame.image.load('src/scenes/select.png')
    gun_image = pygame.image.load('res/images/gun_image.png')
    gun_image = pygame.transform.scale(gun_image, (128, 32))

    current_screen = 'intro'  # Ban đầu, màn hình là intro

    button_rect = pygame.Rect(350, 588, 200, 50)  # Nút PLAY GAME
    button_hover = False  # Biến để kiểm tra xem chuột có hover trên nút không

    back_button_rect = pygame.Rect(50, 550, 200, 50)  # Nút BACK
    back_button_hover = False  # Biến để kiểm tra xem chuột có hover trên nút không

    start_game_button_rect = pygame.Rect(650, 550, 200, 50)  # Nút START
    start_game_button_hover = False  # Biến để kiểm tra xem chuột có hover trên nút không

    choice1_game_button_rect = pygame.Rect(200, 250, 200, 50)  # Nút PvE
    choice1_game_button_hover = False
    choice1_selected = False

    choice2_game_button_rect = pygame.Rect(500, 250, 200, 50)  # Nút PvP
    choice2_game_button_hover = False
    choice2_selected = False

    show_gun_image = False

    # Load font từ file đã tải về
    font = pygame.font.Font('res/fonts/VT323-Regular.ttf', 50)

    start_button_clicked = False
    pve_selected = False
    pvp_selected = False

    while True:
        if current_screen == 'intro':
            show_intro_screen(DISPLAYSURF, intro_screen, button_rect, button_hover, font)
        elif current_screen == 'select':
            show_game_screen(DISPLAYSURF, game_screen, back_button_rect, back_button_hover,
                             start_game_button_rect, start_game_button_hover,
                             choice1_game_button_rect, choice1_game_button_hover, choice1_selected,
                             choice2_game_button_rect, choice2_game_button_hover, choice2_selected,
                             gun_image, show_gun_image, font)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mouse_x, mouse_y = event.pos
                button_hover = button_rect.collidepoint(mouse_x, mouse_y)
                back_button_hover = back_button_rect.collidepoint(mouse_x, mouse_y)
                start_game_button_hover = start_game_button_rect.collidepoint(mouse_x, mouse_y)
                choice1_game_button_hover = choice1_game_button_rect.collidepoint(mouse_x, mouse_y)
                choice2_game_button_hover = choice2_game_button_rect.collidepoint(mouse_x, mouse_y)

            elif event.type == MOUSEBUTTONDOWN:
                if current_screen == 'intro':
                    mouse_x, mouse_y = event.pos
                    if button_rect.collidepoint(mouse_x, mouse_y):
                        current_screen = 'select'
                elif current_screen == 'select':
                    mouse_x, mouse_y = event.pos
                    if back_button_rect.collidepoint(mouse_x, mouse_y):
                        current_screen = 'intro'
                    elif choice1_game_button_rect.collidepoint(mouse_x, mouse_y):
                        choice1_selected = True
                        choice2_selected = False
                        pve_selected = True
                        #show_gun_image = True
                    elif choice2_game_button_rect.collidepoint(mouse_x, mouse_y):
                        choice1_selected = False
                        choice2_selected = True
                        pvp_selected = True
                        #show_gun_image = False
                    elif start_game_button_rect.collidepoint(mouse_x, mouse_y):
                        if pve_selected:
                            start_button_clicked = 1
                        elif pvp_selected:
                            start_button_clicked = 2

        pygame.display.update()

        if start_button_clicked == 1:
            GameScene("PVE")
        elif start_button_clicked == 2:
            GameScene("PVP")

def show_intro_screen(DISPLAYSURF, intro_screen, button_rect, button_hover, font):
    DISPLAYSURF.blit(intro_screen, (0, 0))
    if button_hover:
        pygame.draw.rect(DISPLAYSURF, (128, 128, 128), button_rect, border_radius=10)
    else:
        pygame.draw.rect(DISPLAYSURF, (255, 255, 255), button_rect, border_radius=8, width=2)

    text = font.render('PLAY GAME', True, (255, 255, 255))
    text_rect = text.get_rect(center=button_rect.center)
    DISPLAYSURF.blit(text, text_rect.topleft)

    pygame.display.set_caption('Shooter Battle')

def show_game_screen(DISPLAYSURF, game_screen, back_button_rect, back_button_hover,
                     start_game_button_rect, start_game_button_hover,
                     choice1_game_button_rect, choice1_game_button_hover, choice1_selected,
                     choice2_game_button_rect, choice2_game_button_hover, choice2_selected,
                     gun_image, show_gun_image, font):
    DISPLAYSURF.blit(game_screen, (0, 0))

    if back_button_hover:
        pygame.draw.rect(DISPLAYSURF, (128, 128, 128), back_button_rect, border_radius=10)
    else:
        pygame.draw.rect(DISPLAYSURF, (255, 255, 255), back_button_rect, border_radius=8, width=2)

    text = font.render('BACK', True, (255, 255, 255))
    text_rect = text.get_rect(center=back_button_rect.center)
    DISPLAYSURF.blit(text, text_rect.topleft)

    if start_game_button_hover:
        pygame.draw.rect(DISPLAYSURF, (128, 128, 128), start_game_button_rect, border_radius=10)
    else:
        pygame.draw.rect(DISPLAYSURF, (255, 255, 255), start_game_button_rect, border_radius=8, width=2)

    text = font.render('START', True, (255, 255, 255))
    text_rect = text.get_rect(center=start_game_button_rect.center)
    DISPLAYSURF.blit(text, text_rect.topleft)

    if choice1_game_button_hover:
        pygame.draw.rect(DISPLAYSURF, (128, 128, 128), choice1_game_button_rect, border_radius=10)
    else:
        pygame.draw.rect(DISPLAYSURF, (255, 255, 255), choice1_game_button_rect, border_radius=8, width=2)
    if choice1_selected:
        pygame.draw.rect(DISPLAYSURF, (192, 192, 192), choice1_game_button_rect, border_radius=8)

    text = font.render('PvE', True, (255, 255, 255))
    text_rect = text.get_rect(center=choice1_game_button_rect.center)
    DISPLAYSURF.blit(text, text_rect.topleft)

    if choice2_game_button_hover:
        pygame.draw.rect(DISPLAYSURF, (128, 128, 128), choice2_game_button_rect, border_radius=10)
    else:
        pygame.draw.rect(DISPLAYSURF, (255, 255, 255), choice2_game_button_rect, border_radius=8, width=2)
    if choice2_selected:
        pygame.draw.rect(DISPLAYSURF, (192, 192, 192), choice2_game_button_rect, border_radius=8)

    text = font.render('PvP', True, (255, 255, 255))
    text_rect = text.get_rect(center=choice2_game_button_rect.center)
    DISPLAYSURF.blit(text, text_rect.topleft)

    if show_gun_image:  # Hiển thị hình ảnh gun nếu biến show_gun_image = True
        DISPLAYSURF.blit(gun_image, (200, 350))

    pygame.display.set_caption('Select menu')

if __name__ == "__main__":
    main()
