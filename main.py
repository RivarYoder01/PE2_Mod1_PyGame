#!/user.bin.env python3

"""
The user is presented with music and a menu to choose the level of difficulty, an option to start the game, and an option to quit
circle they must navigate to find a hidden circle. Their circle will change between red and blue depending on if
they are moving closer or further away from the hidden circle

There is a debug key (d) that turns the hidden circle visible (White) and a reset key (r) that relocates the hidden
circle

The game is won when the user puts their circle close enough to the hidden circle that they overlap

Functions in order OF USE:
    main()
    set_difficulty()
    play_music()
    play_game()
    rand_location()
    game_stats()
    set_circle_color
"""

import pygame  # Draws circle and runs the game
import pygame_menu  # Gives the user a menu to pick a difficulty and start the game
import random  # Used to randomize the location
from pygame import mixer

__author__ = 'Rivar Yoder | Andrew Hunhoff'
__version__ = '1.0'
__date__ = '2/18/2024'
__status__ = 'Development'

BLACK = (0, 0, 0)           # Blends the hidden circle in with the background
WHITE = (255, 255, 255)     # Used to show the hidden circle
RED = (255, 0, 0)           # Shows user they are getting closer to the hidden circle
GREEN = (0, 255, 0)         # User's circle changes green when they win the game
BLUE = (0, 0, 255)          # Shows user they are getting further away from the hidden circle

SCREEN_SIZE = 700
SCREEN = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))

game = {
    'circle_size': 50,          # Tells the program how big the circles are
    'move_size': 50,            # How far the circle moves with a keypress
    'prev_x': 0,                # The previous position the user was in through the x-axis
    'prev_y': 0,                # The previous position the user was in through the x-axis
    'user_x': SCREEN_SIZE / 2,  # Places user's circle in the center of the screen (x-axis)
    'user_y': SCREEN_SIZE / 2,  # Places user's circle in the center of the screen (y-axis)
    'hidden_x': 0,              # Randomized number that the hidden circle is placed at (x-axis)
    'hidden_y': 0,              # Randomized number that the hidden circle is placed at (y-axis)
    'user_color': WHITE,        # Will show the user how close they are to the hidden circle
    'hidden_color': BLACK,      # Blends the inner circle in with the black background
    'num_moves': 0,             # Tracks the amount of times the user moves
}

fps_limit = 60  # Shows how often an event happens


def set_difficulty(level, difficulty):
    """
    Takes the user's chosen difficulty setting and changes the distance moved per key press
    :return:
    """
    global game

    if difficulty == 3:  # hardest difficulty - least movement per press
        game['circle_size'], game['move_size'] = (10, 10)
    elif difficulty == 2:  # medium difficulty - a little more movement per key press
        game['circle_size'], game['move_size'] = (25, 25)
    else:  # base difficulty - original move size
        game['circle_size'], game['move_size'] = (50, 50)

    return


def play_music():
    """
    Makes music play while the program is running
    :return:
    """

    pygame.mixer.init()
    pygame.mixer.music.load('Wallpaper.mp3')  # loads the chosen music file
    pygame.mixer.music.set_volume(0.25)  # sets volume for playing music
    pygame.mixer.music.play(loops=-1)  # makes music loop continuously

    return


def play_game():
    """
    Runs the game, a circle will be drawn and placed in the middle of the screen. another 'hidden circle' will be
    randomly placed somewhere in the play area. The user will use the arrow keys to navigate the circle around
    in search of the hidden circle.

    Functions Called:
        rand_location() to put the hidden circle in a random location
        game_stats() to track and display the amount of times the user moves
        set_circle_color() changes the user's circle based on proximity to the hidden circle

    :return:
    """

    clock = pygame.time.Clock()

    run_me = True

    rand_location()  # Function that puts the hidden circle in a random location

    while run_me:  # Constantly runs, records movement from the user
        clock.tick(60)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:  # If quit button is hit, the while loop ends
                run_me = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:  # Moves user's circle left 10 pixels
                    game['user_x'] -= 10
                    game["num_moves"] += 1  # Adds 1 to number of moves used

                if event.key == pygame.K_RIGHT:  # Moves user's circle right 10 pixels
                    game['user_x'] += 10
                    game["num_moves"] += 1  # Adds 1 to number of moves used

                if event.key == pygame.K_DOWN:  # Moves user's circle down 10 pixels
                    game['user_y'] += 10
                    game["num_moves"] += 1  # Adds 1 to number of moves used

                if event.key == pygame.K_UP:  # Moves user's circle up 10 pixels
                    game['user_y'] -= 10
                    game["num_moves"] += 1  # Adds 1 to number of moves used

                if event.key == pygame.K_d:  # Toggles the hidden circle between black and white
                    if game["hidden_color"] == BLACK:
                        game["hidden_color"] = WHITE
                    else:
                        game["hidden_color"] = BLACK

                if event.key == pygame.K_r:  # Puts hidden circle in a new spot
                    rand_location()

        # fill the screen with black (otherwise, the circle will leave a trail)
        SCREEN.fill(BLACK)

        # Draws user's circle and the hidden circle
        game['circle'] = pygame.draw.circle(SCREEN, game['user_color'], (game['user_x'], game['user_y']), 50)
        pygame.draw.circle(SCREEN, game["hidden_color"], (game["hidden_x"], game["hidden_y"]), 50)

        game_stats()  # Shows the user how many times they have moved
        set_circle_color()  # Sets the user circle's color depending on if they are getting closer or further

        pygame.display.flip()


def rand_location():
    """
    randomly generates the position of the hidden circle the user  is trying to find
    :return:
    """
    global game

    user_pos = SCREEN_SIZE / 2  # center of the screen

    inside_dist = game["circle_size"]  # makes sure the hidden circle is not touching the user circle
    outside_dist = SCREEN_SIZE - game["circle_size"]  # stops the hidden circle from touching the edge of the screen

    right_user_dist = user_pos - game["circle_size"]  # makes sure it is at least one circle away on the right
    left_user_dist = user_pos + game["circle_size"]  # makes sure it is at least one circle away on the left

    # continues looping until a valid position is achieved
    while True:

        # the hidden location is not in the center with the user circle and is also  not off screen
        x = random.randint(inside_dist, outside_dist)
        y = random.randint(inside_dist, outside_dist)

        # makes sure the hidden circle is not near the user circle
        if (x < right_user_dist or x > left_user_dist) and (y < right_user_dist or y > left_user_dist):
            game["hidden_x"] = x
            game["hidden_y"] = y
            return


def game_stats():
    """
    Adds text to program screen with Number of moves, debug key and reset key. It shows how many moves have been made
    and what keys to press for the debug mode and to reset the hidden circle location
    :return:
    """
    global game

    font = pygame.font.SysFont(None, 24)  # sets size and font of on-screen text
    # sets shown text and color of text
    line = font.render('# ' + str(game["num_moves"]) + " moves" + " | Debug = D" + " | Reset = R", True, BLUE)

    SCREEN.blit(line, (20, 20))

    return


def set_circle_color():
    """
    When the game is 'won' the user's circle will turn green and the hidden circle will turn white

    Every time the user moves, the new position will be compared to the previous position and the hidden circle's
    position in order to determine whether the user is moving closer (Red) or moving further (Blue) from the
    hidden circle. This is done through the circle's x and y positions therefor there are two if statements that
    run this.

    Then user_x and user_y will replace prev_x and prev_y to be compared once again when the function is called again

    :return:
    """
    global game

    overlap = game['circle_size'] * 2 - 10  # How much the circle must overlap to win the game

    # the users location and the hidden circle's location must be less than the overlap pin order to win.
    if abs(game['user_x'] - game['hidden_x']) < overlap and abs(game['user_y'] - game['hidden_y']) < overlap:
        game['hidden_color'] = WHITE
        game['user_color'] = GREEN

    else:  # If the user is moving towards the hidden circle, the user's circle will be red, if it's moving away,
        # it will be blue
        if game['prev_x'] != game['user_x']:  # Tracking via the x-axis
            # If the previous position is greater than the current position, the user is getting closer
            if abs(game['prev_x'] - game['hidden_x']) > abs(game['user_x'] - game['hidden_x']):
                game['user_color'] = RED
            else:  # Otherwise the circle is getting further
                game['user_color'] = BLUE

        if game['prev_y'] != game['user_y']:  # Tracking via the y-axis
            # If the previous position is greater than the current position, the user is getting closer
            if abs(game['prev_y'] - game['hidden_y']) > abs(game['user_y'] - game['hidden_y']):
                game['user_color'] = RED
            else:  # Otherwise the circle is getting further
                game['user_color'] = BLUE

    game['prev_x'] = game['user_x']  # Resets the previous x-axis with the current position
    game['prev_y'] = game['user_y']  # Resets the previous x-axis with the current position

    return


def main():
    """
    Begins playing music and presents the user with a menu:
        Choose difficulty between Level 1, Level 2, and Level 3
        Play the game, runs play_game()
        Quit, exits the program
    :return:
    """

    play_music()

    pygame.init()

    menu = pygame_menu.Menu('Hot and Cold Game /(^o^)/', 400, 300, theme=pygame_menu.themes.THEME_BLUE)
    menu.add.selector('Difficulty :', [('Level 1', 1), ('Level 2', 2), ('Level 3', 3)], onchange=set_difficulty)
    menu.add.button('Play', play_game)
    menu.add.button('Quit', pygame_menu.events.EXIT)
    menu.mainloop(SCREEN)


if __name__ == '__main__':
    main()
