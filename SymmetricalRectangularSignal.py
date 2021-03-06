from Signal import Signal


class SymmetricalRectangularSignal(Signal):
    def __init__(self, amplitude, start_time, duration_time, period, duty_cycle, frequency):
        super(SymmetricalRectangularSignal, self).__init__(amplitude, start_time, duration_time, frequency, False)
        self.period = period
        self.duty_cycle = duty_cycle

    def f(self, x):
        k = int(x / self.period - self.start_time / self.period)
        if (k * self.period + self.start_time <= x
                and self.duty_cycle* self.period + k * self.period + self.start_time):
            return self.amplitude
        return -self.amplitude
