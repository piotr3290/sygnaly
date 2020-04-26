from Point import Point
from Signal import Signal


class FileManager(object):
    @staticmethod
    def read_file(file_path):
        with open(file_path, 'r') as file:
            start_time = file.readline()
            duration_time = file.readline()
            frequency = file.readline()
            points = file.readline()
            points = points.split()
            signal_points = []
            for i in range(0, len(points), 2):
                signal_point = Point(float(points[i]), float(points[i+1]))
                signal_points.append(signal_point)
            result = Signal(None, start_time, duration_time, frequency)
            result.points = signal_points
            return result

    @staticmethod
    def save_file(file_path, signal):
        with open(file_path, 'w') as file:
            file.write(signal.start_time.__str__() + '\n')
            file.write(signal.duration_time.__str__() + '\n')
            file.write(signal.frequency.__str__() + '\n')
            for point in signal.points:
                file.write(point.__str__() + ' ')
