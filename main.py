#!/user.bin.env python3

"""
DOCSTRING
"""

import pygame
import pygame.mixer
import random

__author__ = 'Rivar Yoder | Andrew Hunhoff'
__version__ = '1.0'
__date__ = '2/18/2024'
__status__ = 'Development'

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

SCREEN_SIZE = screen_width, screen_height = 600, 400
SCREEN = pygame.display.set_mode(SCREEN_SIZE)

# clock = pygame.time.Clock()
fps_limit = 60

global game




def play_game():
    """..."""

    clock = pygame.time.Clock()

    run_me = True

    # circle
    colorcircle = red
    posx = 300
    posy = 200

    other_colorcircle = white
    o_posx = 100
    o_posy = 200

    while run_me:
        clock.tick(60)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run_me = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    posx -= 10

                if event.key == pygame.K_RIGHT:
                    posx += 10

                if event.key == pygame.K_DOWN:
                    posy += 10

                if event.key == pygame.K_UP:
                    posy -= 10

        # fill the screen with black (otherwise, the circle will leave a trail)
        screen.fill(black)

        circle = pygame.draw.circle(screen, colorcircle, (posx, posy), 50)
        pygame.draw.circle(screen, other_colorcircle, (o_posx, o_posy), 50)

        pygame.display.flip()


def main():
    """ ... """

    pygame.init()
    pygame.display.set_caption('Hot and Cold Game 0.0')

    play_game()

    pygame.quit()


if __name__ == '__main__':
    main()
