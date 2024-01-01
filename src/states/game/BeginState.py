from ..BaseState import *
from Dependencies import *

class BeginState(BaseState):
    def __init__(self):
        super(BeginState, self).__init__()
        self.transitionAlpha = 1
        self.next_state = "start"

    def update(self, dt):
        tween.to(self, "transitionAlpha", 0, 1).on_complete(
            tween.to(self, "transitionAlpha", 1, 1).on_complete(
                lambda: setattr(self, 'done', True)
        ))

    def draw(self, surface):
        logo = gTextures['logo']
        logo.set_alpha(1 - self.transitionAlpha)
        surface.blit(logo, logo.get_rect())
        