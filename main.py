#!/user.bin.env python3

"""
DOCSTRING
"""

import pygame
import os, sys, math, pygame, pygame.mixer
from pygame.locals import *

__author__ = 'Rivar Yoder | Andrew Hunhoff'
__version__ = '1.0'
__date__ = '2/18/2024'
__status__ = 'Development'

black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)
run_me = True

screen_size = screen_width, screen_height = 600, 400
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Hot Cold Game :)')

clock = pygame.time.Clock()
fps_limit = 60

#circle
colorcircle = (red)
posx = 300
posy = 200
circle = pygame.draw.circle(screen, colorcircle, (posx, posy), 50)

while run_me:
    clock.tick(fps_limit)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_me = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                posx = posx - 10
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                posx = posx + 10
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                posy = posy + 10
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                posy = posy - 10

    # fill the screen with black (otherwise, the circle will leave a trail)
    screen.fill(black)
    # redraw the circle
    pygame.draw.circle(screen, colorcircle, (posx, posy), 50)

    pygame.display.flip()

pygame.quit()
