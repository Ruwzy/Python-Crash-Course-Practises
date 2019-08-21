import sys

import pygame

def check_keydown_events(event, ship):
    """response the keydown event"""
    if event.key ==pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True

def check_keyup_events(event, ship):
    """response to the keyup event"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events():
    """response for the keyboard and mouse event"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship):
    """update the image on the screen, then change to the new screen."""
    #repaint the screen every time the loop starts
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    #let the last screen can be seen
    pygame.display.flip()


