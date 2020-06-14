from Signal import Signal
from Point import Point
from LowFilter import LowFilter
from copy import deepcopy
import math


class Operation(object):
    @staticmethod
    def convolution(signal1, signal2):
        result_points = []

        for n in range(len(signal1.points) + len(signal2.points) - 1):
            y = 0
            for k in range(len(signal1.points)):
                if 0 <= n - k < len(signal2.points):
                    y += signal1.points[k].y * signal2.points[n - k].y
            result_points.append(Point(n, y))

        result_signal = Signal(None, 0, len(signal1.points) + len(signal2.points) - 1, 1)
        result_signal.points = result_points
        return result_signal

    @staticmethod
    def high_filter(m, f0, fp):
        newf0 = fp / 2 - f0
        low_filter = LowFilter(0, fp, newf0, m)
        low_filter.calculate_points()
        for i in range(m):
            low_filter.points[i].y *= 1 if i % 2 == 0 else -1
        return low_filter

    @staticmethod
    def hanning_window(filter_signal):
        result_signal = deepcopy(filter_signal)
        for i in range(len(result_signal.points)):
            result_signal.points[i].y *= (0.5 - 0.5 * math.cos(2 * math.pi * i / result_signal.m))
        return result_signal

    @staticmethod
    def direct_correlation(signal1, signal2):
        reverse_signal = deepcopy(signal2)
        reverse_signal.points.reverse()
        return Operation.convolution(signal1, reverse_signal)
