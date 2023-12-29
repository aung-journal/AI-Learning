## LIBRARIES
import os
import sys

# Add the "lib" folder to the system path
libs_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "lib")
sys.path.insert(0, libs_folder)

#because we want to import just the file
import pygame
import pyperclip

## SUB_LIBRARIES OF PYGAME
from pygame import mixer

## OTHER FILES(VARs, CLASSEs)
from src.constants import *

## STATE MACHINES
#states(because we want to import the individual classes in this file)
from src.states.gStateStack import StateStack
from src.states.BaseState import BaseState
from src.states.StateMachine import StateMachine

## STATES
from src.states.StartState import *

## MUSIC
gSounds = {
    'start': 'sounds/music.mp3'
}

# dependencies.py

import sys

# List of module names to import
module_names = ['pygame', 'pyperclip', 'src.constants', 'src.states.gStateStack', 'src.states.BaseState', 'src.states.StateMachine', 'src.states.StartState']

# Import the modules dynamically
for module_name in module_names:
    if module_name not in sys.modules:
        __import__(module_name)
