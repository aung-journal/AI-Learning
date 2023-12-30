from Dependencies import *

class BeginState(BaseState):
    def __init__(self):
        super().__init__()

        #set our transistions to be full
        self.transitionAlpha = 1

    def enter(self):
        Timer.tween(1, {
            'self': {'transistionAlpha': 0}
        }, lambda: setattr(self, 'transistionAlpha', 0))
        Timer.tween(1, {
            'self': {'transistionAlpha': 0}
        }, lambda: setattr(self, 'transistionAlpha', 0))
        


        
