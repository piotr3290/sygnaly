import math
from Signal import Signal


class SinusoidalFullWaveSignal(Signal):
    def __init__(self, amplitude, start_time, duration_time, period, frequency):
        super(SinusoidalFullWaveSignal, self).__init__(amplitude, start_time, duration_time, frequency, False)
        self.period = period

    def f(self, x):
        return self.amplitude * math.fabs(math.sin(2 * math.pi / self.period * (x - self.start_time)))
