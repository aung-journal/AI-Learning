class StateStack:
    def __init__(self):
        self.states = []

    def update(self, dt):
        self.states[-1].update(dt)

    def process_ai(self, params, dt):
        self.states[-1].process_ai(params, dt)

    def render(self):
        for state in self.states:
            state.render()

    def clear(self):
        self.states = []

    def push(self, state):
        self.states.append(state)
        state.enter()

    def pop(self):
        self.states[-1].exit()
        self.states.pop()
