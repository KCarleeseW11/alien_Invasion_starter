""" This progrma is made for the design and use of the laser from the rocket
Date 11/15/2026
Kennedy Walker """


import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage the red laser fired from the ship."""

    def __init__(self, game):
        super().__init__()

        self.screen = game.screen
        self.settings = game.settings

        self.rect = pygame.Rect(0, 0, self.settings.bullet_w, self.settings.bullet_h)


        self.rect.midbottom = game.ship.rect.midtop

    
        self.y = float(self.rect.y)

    def update(self):
        """MOVE LASER UP """
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        """LASER DISPLAY ON SCREEN"""
        pygame.draw.rect(self.screen, self.settings.bullet_color, self.rect)
