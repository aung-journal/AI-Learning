from Dependencies import *

class BeginState(BaseState):
    def __init__(self, g_state_machine):
        super().__init__(g_state_machine)

        # Set our transitions to be full
        self.transitionAlpha = 1

    def enter(self):
        tween.to(self, "transitionAlpha", 0, 2).on_complete(
            tween.to(self, "transitionAlpha", 1, 2).on_complete(
                self.gStateMachine.change('begin')
            )
        )

    def update(self, dt):
        Timer.update(dt)

    def render(self, screen):
        gTextures['logo'].set_alpha(1 - self.transitionAlpha)
        screen.blit(gTextures['logo'], gTextures['logo'].get_rect())
