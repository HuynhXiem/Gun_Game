import pygame
import sys
import math  # Thêm thư viện math để tính toán khoảng cách giữa các đối tượng
import random

from .pve_scene import PVE
from ..models.character import Character
from ..models.gun import Gun

class GameScene:
    def __init__(self, type) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        WHITE = (255, 255, 255)

        screen_width = 900
        screen_height = 700
        screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Game bắn súng")
        if (type == "PVE"):
            PVE(screen)

