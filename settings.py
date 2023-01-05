import pygame
import math
import random

# Create the screen dimensions
WIDTH = 1920
HEIGHT = 1080
FPS = 60  # frames per second setting

clock = pygame.time.Clock()  # fps
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # screen

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (150, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YEllOW = (255, 255, 0)
CYAN = (0, 255, 255)
PINK = (255, 0, 255)

blank = pygame.image.load('images\\blank.png')

hangman = [pygame.image.load("images\\bg\\Hangman" + str(i + 1) + ".png") for i in range(10)]

win = pygame.image.load("images\\bg\\Hangman0.png")

fix = pygame.image.load("images\\bg\\Hangman0fix.png")

r = [pygame.image.load("images\\red\\r (" + str(i + 1) + ").png") for i in range(26)]
g = [pygame.image.load("images\\green\\g (" + str(i + 1) + ").png") for i in range(26)]
w = [pygame.image.load("images\\white\\w (" + str(i + 1) + ").png") for i in range(26)]


def image(i, x, y):
    screen.blit(i, (x, y))


# importing the text file
text_file = open("words.txt", "r")
lines = text_file.read().split('\n')

font = pygame.font.Font('font\\comicz.ttf', 65)


# function to determine button click
def button(x, y, w, h, state):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if state == 0:
        if click[0]:
            if x + w > mouse[0] > x and y + h > mouse[1] > y:
                return True
            else:
                return False
    else:
        if x + w > mouse[0] > x and y + h > mouse[1] > y:
            return True
        else:
            return False
