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

# from pygame import event

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

SCREEN_SIZE = 800
SCREEN = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))

game = {
    'circle_size': 50,
    'move_size': 50,
    'prev_x': 0,
    'prev_y': 0,
    'user_x': SCREEN_SIZE / 2,
    'user_y': SCREEN_SIZE / 2,
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

    #  other_colorcircle = WHITE
    #  o_posx = 100
    #  o_posy = 200

    rand_location()

    while run_me:
        clock.tick(60)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run_me = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    posx -= 10
                    game["num_moves"] += 1

                if event.key == pygame.K_RIGHT:
                    posx += 10
                    game["num_moves"] += 1

                if event.key == pygame.K_DOWN:
                    posy += 10
                    game["num_moves"] += 1

                if event.key == pygame.K_UP:
                    posy -= 10
                    game["num_moves"] += 1

                if event.key == pygame.K_d:
                    if game["hidden_color"] == BLACK:
                        game["hidden_color"] = WHITE
                    else:
                        game["hidden_color"] = BLACK

                if event.key == pygame.K_r:
                    rand_location()

        # fill the screen with black (otherwise, the circle will leave a trail)
        SCREEN.fill(BLACK)

        circle = pygame.draw.circle(SCREEN, colorcircle, (posx, posy), 50)
        pygame.draw.circle(SCREEN, game["hidden_color"], (game["hidden_x"], game["hidden_y"]), 50)

        game_stats()


        pygame.display.flip()


def rand_location():
    global game

    user_pos = SCREEN_SIZE / 2

    inside_dist = game["circle_size"]
    outside_dist = SCREEN_SIZE - game["circle_size"]

    right_user_dist = user_pos - game["circle_size"]
    left_user_dist = user_pos + game["circle_size"]

    while True:

        x = random.randint(inside_dist, outside_dist)
        y = random.randint(inside_dist, outside_dist)

        if (x < right_user_dist or x > left_user_dist) and (y < right_user_dist or y > left_user_dist):
            game["hidden_x"] = x
            game["hidden_y"] = y
            return


def game_stats():
    global game

    font = pygame.font.SysFont(None, 24)

    line = font.render('# ' + str(game["num_moves"]) + " moves", True, YELLOW)
    SCREEN.blit(line, (20, 20))

    return


def main():
    """ ... """

    pygame.init()
    pygame.display.set_caption('Hot and Cold Game 0.0')

    play_game()

    pygame.quit()


if __name__ == '__main__':
    main()
