import pygame

class Ship():

    def __init__(self, ai_settings, screen):
        """ initialize the ship and set its original position"""
        self.screen = screen
        self.ai_settings = ai_settings

        # load the ship's image and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # set every new ship to the center of left
        self.rect.center = self.screen_rect.midleft
        self.rect.left = self.screen_rect.left

        #store float type value in setting center
        self.center = float(self.rect.centery)

        # moving signal
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """based on the moving signal to change the ship's position"""
        #update the ship's center value, not the rect
        if self.moving_up and self.rect.top < self.screen_rect.top:
            self.rect.centery += self.ai_settings.ship_speed_fator
        if self.moving_down and self.rect.bottom > 0:
            self.rect.centery -= self.ai_settings.ship_speed_factor

        # update the rect based on the self.center
        self.rect.centery = self.center 

    def blitme(self):
        """ draw the ship at a certain position"""
        self.screen.blit(self.image, self.rect)