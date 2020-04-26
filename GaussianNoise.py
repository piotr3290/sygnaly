from Signal import Signal
import math
import numpy as np


class GaussianNoise(Signal):
    def __init__(self, amplitude, start_time, duration_time, frequency):
        super(GaussianNoise, self).__init__(amplitude, start_time, duration_time, frequency, False)
        self.standard_deviation = 1
        self.mean = 0

    def f(self, x):
        return np.random.normal(0, 1, 1)[0]

