import pygame
import pygame as pg
from pygame import *
import sys
import os
import random
import math
from pygame.locals import *
import time
import pygame_widgets
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox
from pygame_widgets.button import Button


pygame.init()
MOVE_SPEED = 5
WIDTH, HEIGHT = width, height = w, h = 1280, 680 
screen = sc = pygame.display.set_mode((WIDTH, HEIGHT))

cell_x = cell_y = cell = 32

with open('base.txt') as fp2:
    lines = fp2.readlines()