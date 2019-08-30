import pygame

from settings import Settings
from ship import Ship
import game_functions as gf 
from pygame.sprite import Group


def run_game():
    # initialize the pygame, settings and the screen    
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
            (ai_settings.screen_width, ai_settings.screen_height)
    )
    pygame.display.set_caption('Alien Invasion')

    # build a ship
    ship = Ship(ai_settings, screen)

    #build a group to store the bullets
    bullets = Group()

    # start the game's main loop    
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, bullets)

        # let the latest screen can be seen
        pygame.display.flip()

run_game()

