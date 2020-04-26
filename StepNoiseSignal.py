from Signal import Signal
import numpy as np


class StepNoiseSignal(Signal):
    def __init__(self, amplitude, start_time, duration_time, frequency, probability):
        super(StepNoiseSignal, self).__init__(amplitude, start_time, duration_time, frequency)
        self.probability = probability

    def f(self, x):
        return self.amplitude * np.random.choice(np.arange(0, 2), p=[1 - self.probability, self.probability])
