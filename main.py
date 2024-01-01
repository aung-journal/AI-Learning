from Dependencies import *
from States import *

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
states = {
    "begin": BeginState()
}

game = Game(screen, states, "begin")
game.run()

pygame.quit()
sys.exit()