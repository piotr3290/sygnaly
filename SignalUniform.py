from Signal import Signal
import random


class SignalUniform(Signal):
    def __init__(self, amplitude, start_time, duration_time, frequency):
        super(SignalUniform, self).__init__(amplitude, start_time, duration_time, frequency, False)
        self.standard_deviation = 1
        self.mean = 0

    def f(self, x):
        return random.uniform(-self.amplitude, self.amplitude)
