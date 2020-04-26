from Signal import Signal
import math


class SinusoidalHalfWaveSignal(Signal):
    def __init__(self, amplitude, start_time, duration_time, period, frequency):
        super(SinusoidalHalfWaveSignal, self).__init__(amplitude, start_time, duration_time, frequency, False)
        self.period = period

    def f(self, x):
        sinus_value = math.sin(2 * math.pi / self.period * (x - self.start_time))
        return self.amplitude / 2 * (sinus_value + math.fabs(sinus_value))
