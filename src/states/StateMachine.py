class StateMachine:
    def __init__(self, states):
        self.empty = {
            'render': lambda: None,
            'update': lambda dt: None,
            'processAI': lambda params, dt: None,
            'enter': lambda: None,
            'exit': lambda: None
        }
        self.states = states or {}  # [name] -> [function that returns states]
        self.current = self.empty

    def change(self, state_name, enter_params):
        assert state_name in self.states, "State must exist!"
        self.current['exit']()
        self.current = self.states[state_name]()
        self.current['enter'](enter_params)

    def update(self, dt):
        self.current['update'](dt)

    def render(self):
        self.current['render']()

    def process_ai(self, params, dt):
        self.current['processAI'](params, dt)

# #this is our state machine
# gStateMachine = StateMachine({
#     'Begin': BeginState
# })