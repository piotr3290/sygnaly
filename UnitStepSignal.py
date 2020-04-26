from Signal import Signal


class UnitStepSignal(Signal):
    def __init__(self, amplitude, start_time, duration_time, frequency, step_time):
        super(UnitStepSignal, self).__init__(amplitude, start_time, duration_time, frequency, False)
        self.step_time = step_time

    def f(self, x):
        if x > self.step_time:
            return self.amplitude
        elif x == self.step_time:
            return self.amplitude / 2
        return 0
