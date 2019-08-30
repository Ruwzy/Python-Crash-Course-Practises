import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """a class that manage the bullets sent by the ship"""

    def __init__(self, ai_settings, screen, ship):
        """built a bullet in the place of ship"""
        super(Bullet, self).__init__()
        self.screen = screen

        #built a rect of bullet at (0,0), and them set the bullet's position
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        #use float to store the bullet's position
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor


    def update(self):
        """let the bullet move up"""
        # update the bullet's float value
        self.y -= self.speed_factor
        # update the bullet rect's postion
        self.rect.y = self.y


    def draw_bullet(self):
        """draw bullets on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)