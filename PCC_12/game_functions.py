import sys

import pygame

from bullet import Bullet

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """response the keydown event"""
    if event.key ==pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key ==pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)

def fire_bullet(ai_settings, screen, ship, bullets):
    """shot a bullet if haven't reach the limits"""
    #build a bullet, and put it in the bullets Group
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def check_keyup_events(event, ship):
    """response to the keyup event"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings, screen, ship, bullets):
    """response for the keyboard and mouse event"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship, bullets):
    """update the image on the screen, then change to the new screen."""
    #repaint the screen every time the loop starts
    screen.fill(ai_settings.bg_color)

        #redraw all the bullets after the ship and the alien
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()

    # let the last screen can be seen
    pygame.display.flip()

def update_bullets(bullets):
    """update the bullets' position, and delete the disappeared bullets"""
    # update the bullets' position
    bullets.update()

    # delete the disappeared bullets
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets. remove(bullet)