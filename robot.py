import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import math


class Robot:

    def __init__(self, links):
        self.links = links
        self.execute(links)

    def FK(self, th, L):
        L1, L2, L3 = L
        Th1, Th2, Th3 = th
        x0 = 0.0
        y0 = 0.0

        x1 = L1*math.cos(Th1)
        y1 = L1*math.sin(Th1)

        x2 = x1 + L2*math.cos(Th1 + Th2)
        y2 = y1 + L2*math.sin(Th1 + Th2)

        x3 = x2 + L3*math.cos(Th1+Th2+Th3)
        y3 = y2 + L3*math.sin(Th1+Th2+Th3)

        return np.array([[x0, y0], [x1, y1], [x2, y2], [x3, y3]])

    def execute(self, links):
        L1 = 0.5
        L2 = 0.5
        L3 = 0.5

        L = [L1, L2, L3]
        th = [0.0*math.pi, 0.0*math.pi, 0.0*math.pi]

        p = self.FK(th, L)

        fig, ax = plt.subplots()
        plt.title('Forward Kinematics '+str(self.links)+' Links')
        plt.axis('equal')
        plt.subplots_adjust(left=0.1, bottom=0.25)
        plt.xlim([-2.5, 2.5])
        plt.ylim([-2.5, 2.5])

        plt.grid()
        graph, = plt.plot(p.T[0], p.T[1])

        slider1_pos = plt.axes([0.1, 0.13, 0.8, 0.03])
        slider2_pos = plt.axes([0.1, 0.09, 0.8, 0.03])
        slider3_pos = plt.axes([0.1, 0.05, 0.8, 0.03])

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

        def update_th3(slider_val):
            th[2] = slider_val

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
        threshold_slider3 = Slider(
            slider3_pos, 'th3', -1.0*math.pi, 1.0*math.pi, 0.0*math.pi)

        threshold_slider1.on_changed(update_th1)
        threshold_slider2.on_changed(update_th2)
        threshold_slider3.on_changed(update_th3)

        graph.set_linestyle('-')
        graph.set_linewidth(5)
        graph.set_marker('o')
        graph.set_markerfacecolor('g')
        graph.set_markeredgecolor('g')
        graph.set_markersize(15)
        plt.grid()
        plt.show()
