#!/usr/bin/python2.7
'''
Description: This is a simple GUI app which creates a bouncing ball animation.

Created: September 15, 2017
Modified Feb 20, 2020

Author: Blake Vermeer + Chuck Duey
'''

import sys, pygame, os

os.putenv('DISPLAY', ':0')
x = 50
y = 25
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)
pygame.init()

size = width, height = 700, 400
speed = [1, 1]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

# Be careful with this line! The touchscreen doesn't work correctly when hiding the mouse!
pygame.mouse.set_visible(False)

ball = pygame.image.load("./Images/ball.png")
ballrect = ball.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()
