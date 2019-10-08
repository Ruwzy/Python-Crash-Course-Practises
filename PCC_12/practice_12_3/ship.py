import pygame


class Ship():

    def __init__(self, ai_settings, screen):
        """ initialize the ship's setting and its original place"""
        self.screen = screen
        self.ai_settings = ai_settings

        # load the ship's image and the outside rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # set every new ship at the screen's center bottom
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

        # make the ship's setting can sotre float
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)
    

        # moving signal
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """adjust the ship's position based on the moving signal"""
        # upade the center value not the rect value
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.centerx -= self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.top > 0:
            self.centery -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.ai_settings.ship_speed_factor

        self.rect.centerx = self.centerx
        self.rect.centery = self.centery



    def blitme(self):
        """draw a ship at a pointed place"""
        self.screen.blit(self.image, self.rect)
        
