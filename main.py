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

game = {
    'circle_size': 50,
    'move_size': 50,
    'prev_x': 0,
    'prev_y': 0,
    'user_x': SCREEN_SIZE,
    'user_y': SCREEN_SIZE,
    'hidden_x': 0,
    'hidden_y': 0,
    'user_color': WHITE,
    'hidden_color': BLACK,
    'num_moves': 0
}

# clock = pygame.time.Clock()
fps_limit = 60


def play_game():
    """..."""

    clock = pygame.time.Clock()

    run_me = True

    # circle
    colorcircle = RED
    posx = 300
    posy = 200

    other_colorcircle = WHITE
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

                if event.key == pygame.K_d:
                    if other_colorcircle == BLACK:
                        other_colorcircle = WHITE
                    else:
                        other_colorcircle = BLACK

        # fill the screen with black (otherwise, the circle will leave a trail)
        SCREEN.fill(BLACK)

        circle = pygame.draw.circle(SCREEN, colorcircle, (posx, posy), 50)
        pygame.draw.circle(SCREEN, other_colorcircle, (o_posx, o_posy), 50)

        pygame.display.flip()


def main():
    """ ... """

    pygame.init()
    pygame.display.set_caption('Hot and Cold Game 0.0')

    play_game()

    pygame.quit()


if __name__ == '__main__':
    main()
