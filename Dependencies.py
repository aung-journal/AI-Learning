import os
import sys

# Add the "lib" folder to the system path
libs_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "lib")
sys.path.insert(0, libs_folder)

# Import necessary libraries
import pygame
import pyperclip
import tween # this is our actual tweening class
from matplotlib import pyplot

#our classes
from src.constants import *

#states and game classes

#Fonts, Music, Graphics
pygame.init()

gFonts = {
    'medium' : pygame.font.Font('fonts/font.ttf', 24)
}

gTextures = {
    'logo': pygame.image.load('graphics/logo.jpeg')
}