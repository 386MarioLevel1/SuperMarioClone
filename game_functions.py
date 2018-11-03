import sys
import pygame


def check_events(ai_settings, screen):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(ai_settings, screen, mario, map):
    # Redraw the screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)

    mario.blitme()

    map.blitme()

    pygame.display.flip()
