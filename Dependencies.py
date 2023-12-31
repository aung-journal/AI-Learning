import os
import sys

# Add the "lib" folder to the system path
libs_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "lib")
sys.path.insert(0, libs_folder)

# Import necessary libraries
import pygame
import pyperclip
import tween # this is our actual tweening class

## SUB_LIBRARIES OF PYGAME
# (No need to import again since pygame and mixer are already imported)
from pygame import mixer

## SERVICES
from src.services.timer import * # tweening and timer classes

## OTHER FILES(VARs, CLASSEs)
from src.constants import *

## STATE MACHINES
# states(because we want to import the individual classes in this file)
from src.states.StateMachine import *
from src.states.gStateStack import *
from src.states.BaseState import *

## MUSIC
mixer.init()
gSounds = {
    'music': pygame.mixer.Sound('sounds/music.mp3')
}

## Art
gTextures = {
    'logo': pygame.image.load('graphics/logo.jpeg')
}

# # Import modules dynamically
# module_names = ['pygame', 'pyperclip', 'src.constants', 'src.states.gStateStack', 'src.states.BaseState', 'src.states.StateMachine']

# for module_name in module_names:
#     if module_name not in sys.modules:
#         __import__(module_name)
