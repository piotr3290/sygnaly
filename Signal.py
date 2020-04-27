from Point import Point
from copy import deepcopy
import math


class Signal(object):
    def __init__(self, amplitude, start_time, duration_time, frequency, is_discrete=True):
        self.amplitude = amplitude
        self.start_time = start_time
        self.duration_time = duration_time
        self.frequency = frequency
        self.points = []
        self.is_discrete = is_discrete

    def calculate_points(self):
        n = int(self.frequency * self.duration_time) + 1
        distance_between_points = self.duration_time / (n - 1)
        for i in range(n):
            x = self.start_time + i * distance_between_points
            self.points.append(Point(x, self.f(x)))

    def f(self, x):
        pass

    def operators_function(self, signal, operation):
        result_points = []
        signal_points = signal.points

        for i in range(len(self.points)):
            while len(signal_points) > 0 and self.points[i].x > signal_points[0].x:
                result_points.append(deepcopy(signal_points[0]))
                signal_points.pop(0)
            if len(signal_points) > 0 and self.points[i].x == signal_points[0].x:
                y = operation(self.points[i].y, signal_points[0].y)
                if y is not None:
                    result_points.append(Point(self.points[i].x, y))
                signal_points.pop(0)
            else:
                result_points.append(deepcopy(self.points[i]))
        for point in signal_points:
            result_points.append(deepcopy(point))
        result_start_time = min(self.start_time, signal.start_time)
        result_duration = max(self.start_time + self.duration_time,
                              signal.start_time + signal.duration_time) - result_start_time
        result_signal = Signal(None, result_start_time, result_duration, None)
        result_signal.points = result_points
        return result_signal

    def __add__(self, signal):
        def operation(a, b):
            return a + b

        return self.operators_function(signal, operation)

    def __mul__(self, signal):
        def operation(a, b):
            return a * b

        return self.operators_function(signal, operation)

    def __sub__(self, signal):
        def operation(a, b):
            return a - b

        return self.operators_function(signal, operation)

    def __truediv__(self, signal):
        def operation(a, b):
            if b == 0:
                return None
            return a / b

        return self.operators_function(signal, operation)

    def mean(self):
        return sum(point.y for point in self.points) / len(self.points)

    def abs_mean(self):
        return sum(abs(point.y) for point in self.points) / len(self.points)

    def average_power(self):
        return sum(pow(point.y, 2) for point in self.points) / len(self.points)

    def variance(self):
        mean = self.mean()
        return sum(pow(point.y - mean, 2) for point in self.points) / len(self.points)

    def root_mean_square(self):
        return math.sqrt(self.average_power())

    def sampling(self, Ts):
        result_points = []
        n = int(1 / Ts * self.duration_time) + 1
        distance_between_points = self.duration_time / (n - 1)
        for i in range(n):
            x = self.start_time + i * distance_between_points
            result_points.append(Point(x, self.f(x)))
        return result_points

    def quantization(self, Ts, n_bits):
        result_points = self.sampling(Ts)
        mini = min(point.y for point in self.points)
        maxi = max(point.y for point in self.points)
        hop = (abs(maxi - mini)) / (pow(2, n_bits) - 1)
        hops = []

        for i in range(0, pow(2, n_bits)):
            hops.append(mini + i * hop)

        for i in range(0, len(result_points)):
            hop_index = 0
            closest_value = abs(hops[0] - result_points[i].y)
            for j in range(1, len(hops)):
                if abs(hops[j] - result_points[i].y) < closest_value:
                    closest_value = abs(hops[j] - result_points[i].y)
                    hop_index = j
            result_points[i].y = hops[hop_index]

        return result_points
