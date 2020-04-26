from Signal import Signal


class UnitImpulseSignal(Signal):
    def __init__(self, amplitude, start_time, duration_time, frequency, sample_number):
        super(UnitImpulseSignal, self).__init__(amplitude, start_time, duration_time, frequency)
        self.sample_number = sample_number

    def f(self, x):
        if (x - self.start_time) * self.frequency == self.sample_number:
            return self.amplitude
        return 0
