import pygame

from settings import Settings
from ship import Ship
import game_functions as gf 


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

    # start the game's main loop    
    while True:
        gf.check_events(ship)
        ship.update()
        gf.check_events()
        gf.update_screen(ai_settings, screen, ship)

        # let the latest screen can be seen
        pygame.display.flip()

run_game()

