import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """build a bullet at the position of ship"""
    
    def __init__(self, ai_settings, screen, ship):
        """build a bullet at the position of the ship"""
        super(Bullet, self).__init__()
        self.screen = screen

        # build a rect to represent a bullet at (0,0), then set the bullet's position to the right place
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.right = ship.rect.right

        # use float to store the bullet's position
        self.x = float(self.rect.x)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """make the bullet shoot to the right"""
        # update the float data of the bullet's position
        self.x += self.speed_factor
        # update the rect of the bullet's position
        self.rect.x = self.x

    def draw_bullet(self):
        """draw the bullet on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)

    