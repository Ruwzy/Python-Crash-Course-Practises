import sys

import pygame


def check_keydown_events(event, ship):
    """response to the keydown"""
    if event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True

def check_keyup_events(event, ship):
    """response to the keyup"""
    if event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False

def check_events(ship):
    """response to the keyboard and the mouse"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def update_screen(ai_settings, screen, ship):
    """update the screen's image, and change to the new screen"""
    # Redraw the screen each time starts the loop
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # show the lastest drawing screen
    pygame.display.flip()