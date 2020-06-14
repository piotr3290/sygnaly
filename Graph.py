import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


class Graph:
    @staticmethod
    def draw(signal, path, interval_amount):
        data_frame = pd.DataFrame(data=([point.x, point.y] for point in signal.points), columns=['time', 'signal'])
        if signal.is_discrete:
            sns.relplot(x="time", y="signal", data=data_frame)
        else:
            sns.relplot(x="time", y="signal", data=data_frame, kind="line")
        plt.savefig("signalGraph" + path)
        plt.close()
        # y = np.array(list(point.y for point in signal.points))
        # sns.distplot(y, bins=interval_amount, kde=False, hist_kws=dict(edgecolor="black", linewidth=1))
        # plt.savefig("signalHistogram" + path)
        # plt.close()

    @staticmethod
    def draw_quantization(signal_analog, signal_quantization, path, ro=False):
        data_frame_analog = pd.DataFrame(data=([point.x, point.y] for point in signal_analog.points),
                                         columns=['time', 'signal'])
        data_frame_quantization = pd.DataFrame(data=([point.x, point.y] for point in signal_quantization.points),
                                               columns=['time', 'signal'])
        fig = plt.figure()
        plt.plot(data_frame_analog['time'], data_frame_analog['signal'])
        if ro:
            plt.plot(data_frame_quantization['time'], data_frame_quantization['signal'], 'ro')
        else:
            plt.plot(data_frame_quantization['time'], data_frame_quantization['signal'])
        plt.xlabel('time [s]')
        plt.ylabel('signal')
        plt.savefig("signalGraph" + path)
