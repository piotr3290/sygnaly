from Signal import Signal
import math


class LowFilter(Signal):
    def __init__(self, start_time, frequency, f0, m):
        super(LowFilter, self).__init__(None, start_time, m-1, 1, True)
        self.m = m
        self.f0 = f0
        self.k = frequency / f0

    def f(self, x):
        if x == (self.m - 1) / 2:
            return 2 / self.k
        else:
            return math.sin(2 * math.pi * (x - (self.m - 1) / 2)/self.k) / (math.pi * (x - (self.m - 1) / 2))
