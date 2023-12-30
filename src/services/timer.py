#EXAMPLE USAGE:
# # Create a dictionary defining the initial and final values for tweening
# tween_definition = {
#     {'target': {'x': 50}, 'values': {'x': 500}},
#     {'target': {'y': 50}, 'values': {'y': 400}}
# }

# # Create a Tween timer with a duration of 2000 milliseconds (2 seconds)
# tween_timer = Timer.tween(2000, tween_definition)

# # Update the tween timer
# Timer.update(dt)


class Timer:
    defaultGroup = []

    def __init__(self):
        self.elapsed = 0
        self.group = self.group
        self.remove = self.remove
        self.register = self.register
        self.lastGroup = self.defaultGroup

    @staticmethod
    def group(timer, group=None):
        if not group:
            group = Timer.defaultGroup
        Timer.attach(group, timer)
        return timer

    def remove(self):
        if self.group:
            Timer.detach(self.group, self)
        return self

    def register(self):
        Timer.attach(self.lastGroup, self)
        return self

    def limit(self, limitField):
        self.limitField = limitField
        return self

    def finish(self, finishField):
        self.finishField = finishField
        return self

    def ease(self, easeField):
        self.easeField = easeField
        return self

    def updateContinuous(self, dt):
        cutoff = self.cutoff
        elapsed = self.elapsed + dt

        if self.callback(dt) == False or elapsed >= cutoff:
            if self.finishField:
                self.finishField(elapsed - cutoff)
            self.remove()

        self.elapsed = elapsed

    def updateIntermittent(self, dt):
        duration = self.delay or self.interval
        elapsed = self.elapsed + dt

        while elapsed >= duration:
            elapsed -= duration
            if self.limitField:
                self.limitField -= 1
            if self.callback(elapsed) == False or self.delay or self.limitField == 0:
                if self.finishField:
                    self.finishField(elapsed)
                self.remove()
                return

        self.elapsed = elapsed

    def updateTween(self, dt):
        elapsed = self.elapsed + dt
        plan = self.plan
        duration = self.duration

        self.elapsed = elapsed

        if elapsed >= duration:
            for index in range(len(plan)):
                task = plan[index]
                task['target'][task['key']] = task['final']
            if self.finishField:
                self.finishField(elapsed - duration)
            self.remove()
            return

        ease = self.easeField

        for index in range(len(plan)):
            task = plan[index]
            target, key = task['target'], task['key']
            initial, change = task['initial'], task['change']

            target[key] = ease(elapsed, initial, change, duration)

    def callback(self, dt):
        # Add your callback logic here
        pass

    @staticmethod
    def planTween(definition):
        plan = []

        for target, values in definition.items():
            for key, final in values.items():
                initial = target[key]

                plan.append({
                    'target': target,
                    'key': key,
                    'initial': initial,
                    'final': final,
                    'change': final - initial,
                })

        return plan

    @staticmethod
    def easeLinear(elapsed, initial, change, duration):
        return change * elapsed / duration + initial

    @staticmethod
    def attach(group, item):
        if item.group:
            Timer.detach(item.group, item)

        index = len(group) + 1
        item.index = index
        group.append(item)
        item.group = group
        item.lastGroup = group

    @staticmethod
    def detach(group, item):
        index = item.index
        group[index - 1] = group[-1]
        group[index - 1]['index'] = index
        group.pop()

    @staticmethod
    def update(dt, group=None):
        if not group:
            group = Timer.defaultGroup
        for index in range(len(group), 0, -1):
            group[index - 1].update(dt)

    @staticmethod
    def clear(group=None):
        if not group:
            group = Timer.defaultGroup
        for i in range(len(group)):
            group[i] = None

    @staticmethod
    def Tween(duration, definition):
        return Timer.initialize({
            'duration': duration,
            'plan': Timer.planTween(definition),
            'update': Timer.updateTween,
            'easeField': Timer.easeLinear,
            'ease': Timer.ease,
            'finish': Timer.finish,
        })

    @staticmethod
    def After(delay, callback):
        return Timer.initialize({
            'delay': delay,
            'callback': callback,
            'update': Timer.updateIntermittent,
        })

    @staticmethod
    def Every(interval, callback):
        return Timer.initialize({
            'interval': interval,
            'callback': callback,
            'update': Timer.updateIntermittent,
            'limit': Timer.limit,
            'finish': Timer.finish,
        })

    @staticmethod
    def Prior(cutoff, callback):
        return Timer.initialize({
            'cutoff': cutoff,
            'callback': callback,
            'update': Timer.updateContinuous,
            'finish': Timer.finish,
        })

    @staticmethod
    def initialize(timer):
        timer['elapsed'] = 0
        timer['group'] = Timer.group
        timer['remove'] = Timer.remove
        timer['register'] = Timer.register

        Timer.attach(Timer.defaultGroup, timer)

        return timer
