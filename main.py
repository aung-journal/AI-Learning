from Dependencies import *
from STATES import *

pygame.init()
mixer.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
running = True
dt = 0

while running:
    dt = clock.tick(60) / 1000.0  # Convert milliseconds to seconds

    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:
            running = False

    #the display to put your work on screen
    pygame.display.flip()

    #limit fps to 60
    clock.tick(60)

pygame.quit()



