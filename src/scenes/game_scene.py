import pygame
import sys
import math  # Thêm thư viện math để tính toán khoảng cách giữa các đối tượng
import random

from .pve_scene import PVE
<<<<<<< HEAD

=======
>>>>>>> 89bfd9329720951d116fc596b44ebe742bef4c79
from ..models.character import Character
from ..models.gun import Gun

class GameScene:
    def __init__(self, type) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
<<<<<<< HEAD

=======
        WHITE = (255, 255, 255)
>>>>>>> 89bfd9329720951d116fc596b44ebe742bef4c79

        screen_width = 900
        screen_height = 700
        screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Game bắn súng")
<<<<<<< HEAD

        if (type == "PVE"):
            pve_scene = PVE(screen)
            while pve_scene.running:
                pve_scene.check_game_over()
                pve_scene.run_pve()
=======
        if (type == "PVE"):
            PVE(screen)

>>>>>>> 89bfd9329720951d116fc596b44ebe742bef4c79
