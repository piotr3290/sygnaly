from Signal import Signal
from copy import deepcopy
from Point import Point
import math


class Converter(object):

    def __init__(self):
        pass

    @staticmethod
    def quantization(signal, Ts, n_bits):
        result_signal = Signal(None, None, None, None)
        result_signal.points = signal.quantization(Ts, n_bits)
        signal_to_draw = Signal(None, None, None, None, False)
        signal_to_draw.points.append(signal.points[0])
        new_ts = Ts / 2
        for i in range(1, len(signal.points)):
            signal_to_draw.points.append(Point(signal.points[i - 1].x + new_ts, signal.points[i - 1].y))
            signal_to_draw.points.append(Point(signal.points[i - 1].x + new_ts, signal.points[i].y))
        signal_to_draw.points.append(signal.points[-1])
        return result_signal, signal_to_draw

    @staticmethod
    def zoh(self, signal):
        reconstructed_signal = Signal(None, None, None, None, False)
        reconstructed_signal.points.append(signal.points[0])
        for i in range(1, len(signal.points)):
            reconstructed_signal.points.append(Point(signal.points[i].x, signal.points[i - 1].y))
            reconstructed_signal.points.append(signal.points[i])
        return reconstructed_signal

    @staticmethod
    def foh(self, signal):
        reconstructed_signal = Signal(None, None, None, None, False)
        reconstructed_signal.points = deepcopy(signal.points)
        return reconstructed_signal

    @staticmethod
    def sinc(self, x):
        if x != 0:
            return math.sin(math.pi * x) / (math.pi * x)
        else:
            return 1

    # @staticmethod
    # def sinc_reconsctruct(self, signal):
