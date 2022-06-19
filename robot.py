import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import math


class Robot:

    def __init__(self, links):
        self.links = links
        self.execute(links)

    def FK(self, th, L):
        L1, L2 = L
        Th1, Th2 = th
        x0 = 0.0
        y0 = 0.0

        x1 = L1*math.cos(Th1)
        y1 = L1*math.sin(Th1)

        x2 = x1 + L2*math.cos(Th1 + Th2)
        y2 = y1 + L2*math.sin(Th1 + Th2)

        return np.array([[x0, y0], [x1, y1], [x2, y2]])

    def execute(self, links):
        L1 = 0.5
        L2 = 0.5

        L = [L1, L2]
        th = [0.0*math.pi, 0.5*math.pi]

        p = self.FK(th, L)
        fig, ax = plt.subplots()
        plt.title('Forward Kinematics 2 Links')
        plt.axis('equal')
        plt.subplots_adjust(left=.1, bottom=0.15)
        plt.xlim([-1.3, 1.3])
        plt.ylim([-1.3, 1.3])
        plt.grid()
        graph, = plt.plot(p.T[0], p.T[1])

        slider1_pos = plt.axes([0.1, 0.05, 0.8, 0.03])
        slider2_pos = plt.axes([0.1, 0.01, 0.8, 0.03])

        def update_th1(slider_val):
            th[0] = slider_val

            p = self.FK(th, L)

            graph.set_data(p.T[0], p.T[1])
            graph.set_linestyle('-')
            graph.set_linewidth(5)
            graph.set_marker('o')
            graph.set_markerfacecolor('g')
            graph.set_markeredgecolor('g')
            graph.set_markersize(15)

            fig.canvas.draw_idle()

        def update_th2(slider_val):
            th[1] = slider_val

            p = self.FK(th, L)

            graph.set_data(p.T[0], p.T[1])
            graph.set_linestyle('-')
            graph.set_linewidth(5)
            graph.set_marker('o')
            graph.set_markerfacecolor('g')
            graph.set_markeredgecolor('g')
            graph.set_markersize(15)

            fig.canvas.draw_idle()

        threshold_slider1 = Slider(
            slider1_pos, 'th1', -1.0*math.pi, 1.0*math.pi, 0.0*math.pi)
        threshold_slider2 = Slider(
            slider2_pos, 'th2', -1.0*math.pi, 1.0*math.pi, 0.0*math.pi)

        threshold_slider1.on_changed(update_th1)
        threshold_slider2.on_changed(update_th2)

        graph.set_linestyle('-')
        graph.set_linewidth(5)
        graph.set_marker('o')
        graph.set_markerfacecolor('g')
        graph.set_markeredgecolor('g')
        graph.set_markersize(15)
        plt.grid()
        plt.show()
