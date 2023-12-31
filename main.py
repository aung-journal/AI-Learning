from Dependencies import *
from STATES import *

pygame.init()
mixer.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
running = True
dt = 0

# This is our state machine
gStateMachine = StateMachine({
    'begin': lambda: BeginState(gStateMachine)
})

def update(dt):
    gStateMachine.update(dt)

def render(screen):
    gStateMachine.render(screen)

while running:
    dt = clock.tick(60) / 1000.0  # Convert milliseconds to seconds

    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False

    #playing sound
    gSounds['music'].play()

    update(dt)

    # Clear the screen
    screen.fill((255, 255, 255))

    # Render and update the display
    render(screen)
    pygame.display.flip()

    # Limit FPS to 60
    clock.tick(60)

pygame.quit()
