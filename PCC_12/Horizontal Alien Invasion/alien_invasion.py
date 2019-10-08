import sys

import pygame

from pygame.sprite import Group

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

    # build a group to store the bullets
    bullets = Group()

 # Start the game's main loop
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        gf.update_screen(ai_settings, screen, ship, bullets)

run_game()
