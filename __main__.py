import seaborn as sns
from Signal import Signal
from RectangularSignal import RectangularSignal
from SignalUniform import SignalUniform
from SinusoidalFullWaveSignal import SinusoidalFullWaveSignal
from SinusoidalHalfWaveSignal import SinusoidalHalfWaveSignal
from StepNoiseSignal import StepNoiseSignal
from SymmetricalRectangularSignal import SymmetricalRectangularSignal
from TriangularSignal import TriangularSignal
from UnitImpulseSignal import UnitImpulseSignal
from UnitStepSignal import UnitStepSignal
from GaussianNoise import GaussianNoise
from SinusoidalSignal import SinusoidalSignal
from FileManager import FileManager
from Graph import Graph
import matplotlib.pyplot as plt
import pandas as pd
from Converter import Converter
from Operation import Operation
from LowFilter import LowFilter

if __name__ == "__main__":
    s = SinusoidalSignal(amplitude=1, start_time=0, duration_time=5, frequency=20, period=0.3)  # f=0.2
    s.calculate_points()
    s2 = SinusoidalSignal(amplitude=0.2, start_time=0, duration_time=5, frequency=20, period=5)  # f=5
    s2.calculate_points()
    # splot = Operation.convolution(s, s2)
    # korelacja = Operation.direct_correlation(s, s2)
    filtr = LowFilter(0, 50, 2, 25)
    filtr.calculate_points()
    filtr2 = Operation.high_filter(31, 2, 50)
    # # print(splot.points)

    Graph.draw(s, 'poczatkowy3', 10)
    Graph.draw(s2, 'szum3', 10)
    s3 = s + s2
    Graph.draw(s3, 'zaklocony3', 10)

    Graph.draw(Operation.convolution(Operation.hanning_window(filtr2), s3), 'filtracjagornaokno3', 10)

    # s = StepNoiseSignal(amplitude=15, start_time=0, duration_time=20, frequency=10, probability=0.2)
    # s.calculate_points()
    # s2 = SinusoidalSignal(amplitude=15, start_time=0, duration_time=20, frequency=100, period=5)
    # s2.calculate_points()
    # # FileManager.save_file('nowy.txt', s)
    # Graph.draw(s, 'rec', 5)
    # Graph.draw(s2, 'sin', 5)
    # print("Wartość średnia: " + s.mean().__str__())
    # print("Wartość średnia bezwzględna: " + s.abs_mean().__str__())
    # print("Średnia moc: " + s.average_power().__str__())
    # print("Wariancja: " + s.variance().__str__())
    # print("Wartość skuteczna: " + s.root_mean_square().__str__())
    #
    #
    # print("Wartość średnia: " + s2.mean().__str__())
    # print("Wartość średnia bezwzględna: " + s2.abs_mean().__str__())
    # print("Średnia moc: " + s2.average_power().__str__())
    # print("Wariancja: " + s2.variance().__str__())
    # print("Wartość skuteczna: " + s2.root_mean_square().__str__())
    # # s = FileManager.read_file("nowy.txt")
    # s = s-s2
    # s.is_discrete = False
    # print("Wartość średnia: " + s.mean().__str__())
    # print("Wartość średnia bezwzględna: " + s.abs_mean().__str__())
    # print("Średnia moc: " + s.average_power().__str__())
    # print("Wariancja: " + s.variance().__str__())
    # print("Wartość skuteczna: " + s.root_mean_square().__str__())
    # Graph.draw(s, 'mul', 5)

    # s = SinusoidalSignal(amplitude=15, start_time=0, duration_time=1, frequency=1000, period=1/4)
    # s.calculate_points()
    # ts = 1/3
    # samples = s.sampling(ts)
    # sam_signal = Signal(None, None, None, None)
    # sam_signal.points = samples
    # s2, s3 = Converter.quantization(s, ts, 3)
    # s4, s5, s6 = Converter.foh(s2), Converter.zoh(s2), Converter.sinc_recostruct(s2, 100, 50)
    #
    # Graph.draw_quantization(s, s2, 'quantsin4', True)
    # Graph.draw_quantization(s, s4, 'fohsin')
    # Graph.draw_quantization(s, s5, 'zohsin')
    # Graph.draw_quantization(s, s6, 'sincsin4')
    # print("sredniokwadratowy: ", Converter.mean_squared_error(sam_signal, s2))
    # print("stosunek szum-sygnal: ", Converter.signal_to_noise_ratio(sam_signal, s2))
    # print("max-diff: ", Converter.maximum_difference(sam_signal, s2))
