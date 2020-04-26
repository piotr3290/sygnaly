from Signal import Signal
import math


class SinusoidalSignal(Signal):
    def __init__(self, amplitude, start_time, duration_time, period, frequency):
        super(SinusoidalSignal, self).__init__(amplitude, start_time, duration_time, frequency, False)
        self.period = period

    def f(self, x):
        return self.amplitude * math.sin(2 * math.pi / self.period * (x - self.start_time))
