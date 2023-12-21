import os
import sys

# Add the "lib" folder to the system path
libs_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "lib")
sys.path.insert(0, libs_folder)

import pygame
