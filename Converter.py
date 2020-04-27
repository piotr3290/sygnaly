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
    def zoh(signal):
        reconstructed_signal = Signal(None, None, None, None, False)
        reconstructed_signal.points.append(signal.points[0])
        for i in range(1, len(signal.points)):
            reconstructed_signal.points.append(Point(signal.points[i].x, signal.points[i - 1].y))
            reconstructed_signal.points.append(signal.points[i])
        return reconstructed_signal

    @staticmethod
    def foh(signal):
        reconstructed_signal = Signal(None, None, None, None, False)
        reconstructed_signal.points = deepcopy(signal.points)
        return reconstructed_signal

    @staticmethod
    def sinc(x):
        if x != 0:
            return math.sin(math.pi * x) / (math.pi * x)
        else:
            return 1

    @staticmethod
    def find_nearest_neighbours(points, t):
        left_neighbour_index = None
        for i in range(0, len(points)):
            if t < points[i].x:
                break
            left_neighbour_index = i
        return left_neighbour_index

    @staticmethod
    def point_for_sinc_reconstruct(points, t_s, t, neighbors_number):
        sum = 0
        left_neighbour_index = Converter.find_nearest_neighbours(points, t)
        for i in range(neighbors_number):
            if left_neighbour_index - i >= 0:
                sum += points[left_neighbour_index - i].y * Converter.sinc(t / t_s - left_neighbour_index + i)
            if left_neighbour_index + i + 1 < len(points):
                sum += points[left_neighbour_index + 1 + i].y * Converter.sinc(t / t_s - left_neighbour_index - i - 1)
        return sum

    @staticmethod
    def sinc_recostruct(signal, frequency, neighbors_number):
        start_time = signal.points[0].x
        t_s = signal.points[1].x - start_time
        duration_time = signal.points[-1].x - start_time
        n = int(frequency * duration_time) + 1
        distance_between_points = duration_time / (n - 1)
        signal_reconstructed = Signal(None, start_time, duration_time, frequency, False)
        for i in range(n):
            x = start_time + i * distance_between_points
            signal_reconstructed.points.append(
                Point(x, Converter.point_for_sinc_reconstruct(signal.points, t_s, x, neighbors_number)))
        return signal_reconstructed

    @staticmethod
    def mean_squared_error(signal_original, signal_quantified):
        result = 0
        for i in range(len(signal_quantified.points)):
            result += pow(signal_original.points[i].y - signal_quantified.points[i].y, 2)
        return result / len(signal_quantified.points)

    @staticmethod
    def signal_to_noise_ratio(signal_original, signal_quantified):
        sum_up = 0
        sum_down = 0
        for i in range(len(signal_quantified.points)):
            sum_up += pow(signal_original.points[i].y, 2)
            sum_down += pow(signal_original.points[i].y - signal_quantified.points[i].y, 2)
        return 10 * math.log(sum_up / sum_down, 10)

    @staticmethod
    def maximum_difference(signal_original, signal_quantified):
        return max(abs(signal_original.points[i].y - signal_quantified.points[i].y) for i in
                   range(1, len(signal_quantified.points)))
