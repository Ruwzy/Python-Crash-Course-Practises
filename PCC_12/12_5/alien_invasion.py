import sys

import pygame

from settings import Settings

from ship import Ship

import game_functions as gf 


def run_game():
    """ initialize the game and creat a screen"""
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien_Invasion")

    # built a ship
    ship = Ship(ai_settings, screen)

 # Start the game's main loop
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)

run_game()
