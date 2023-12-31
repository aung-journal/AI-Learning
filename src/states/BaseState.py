class BaseState:
    def __init__(self, g_state_machine):
        self.gStateMachine = g_state_machine
        pass

    def enter(self):
        pass

    def exit(self):
        pass

    def update(self, dt):
        pass

    def render(self, screen):
        pass
