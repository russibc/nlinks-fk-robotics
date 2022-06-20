import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import math


class Robot:

    def __init__(self, links):
        if(links <= 0 or links > 3):
            print('Invalid number of links')
        else:
            self.links = links
            self.execute()

    def FK(self, th, L):
        x0 = 0.0
        y0 = 0.0

        x1 = L[0]*math.cos(th[0])
        y1 = L[0]*math.sin(th[0])

        if(self.links == 2):
            x2 = x1 + L[1]*math.cos(th[0] + th[1])
            y2 = y1 + L[1]*math.sin(th[0] + th[1])
        elif(self.links == 3):
            x2 = x1 + L[1]*math.cos(th[0] + th[1])
            y2 = y1 + L[1]*math.sin(th[0] + th[1])

            x3 = x2 + L[2]*math.cos(th[0]+th[1]+th[2])
            y3 = y2 + L[2]*math.sin(th[0]+th[1]+th[2])

        X = []
        if(self.links == 1):
            X = np.array([[x0, y0], [x1, y1]])
        elif(self.links == 2):
            X = np.array([[x0, y0], [x1, y1], [x2, y2]])
        elif(self.links == 3):
            X = np.array([[x0, y0], [x1, y1], [x2, y2], [x3, y3]])

        return X

    def defineL(self):
        L = []
        while(len(L) != self.links):
            L.append(0.5)
        return L

    def updateGraphic(self, text, fig, graph, p):
        graph.set_data(p.T[0], p.T[1])
        graph.set_linestyle('-')
        graph.set_linewidth(5)
        graph.set_marker('o')
        graph.set_markerfacecolor('g')
        graph.set_markeredgecolor('g')
        graph.set_markersize(15)
        fig.canvas.draw_idle()
        text.set_text(
            'x = '+str(round(p.T[0][self.links], 2))+', y =' + str(round(p.T[1][self.links], 2)))

    def execute(self):
        slider1_pos = 0
        slider2_pos = 0
        slider3_pos = 0

        L = self.defineL()

        th = [0.0*math.pi, 0.0*math.pi, 0.0*math.pi]

        p = self.FK(th, L)

        fig, ax = plt.subplots()
        plt.title('Forward Kinematics '+str(self.links) +
                  ' Link'+('s' if self.links > 1 else ''))
        plt.axis('equal')
        plt.subplots_adjust(left=0.1, bottom=0.25)
        plt.xlim([-2.5, 2.5])
        plt.ylim([-2.5, 2.5])
        plt.grid()
        graph, = plt.plot(p.T[0], p.T[1])
        text = ax.text(.8, .8, 'x = '+str(
            round(p.T[0][self.links], 2))+', y =' + str(round(p.T[1][self.links], 2)))

        def update_th1(slider_val):
            th[0] = slider_val
            p = self.FK(th, L)
            self.updateGraphic(text, fig, graph, p)

        def update_th2(slider_val):
            th[1] = slider_val
            p = self.FK(th, L)
            self.updateGraphic(text, fig, graph, p)

        def update_th3(slider_val):
            th[2] = slider_val
            p = self.FK(th, L)
            self.updateGraphic(text, fig, graph, p)

        slider1_pos = plt.axes([0.1, 0.13, 0.8, 0.03])
        threshold_slider1 = Slider(
            slider1_pos, 'th1', -1.0*math.pi, 1.0*math.pi, 0.0*math.pi)
        threshold_slider1.on_changed(update_th1)

        if(self.links == 2):
            slider2_pos = plt.axes([0.1, 0.09, 0.8, 0.03])
            threshold_slider2 = Slider(
                slider2_pos, 'th2', -1.0*math.pi, 1.0*math.pi, 0.0*math.pi)
            threshold_slider2.on_changed(update_th2)
        elif(self.links == 3):
            slider2_pos = plt.axes([0.1, 0.09, 0.8, 0.03])
            threshold_slider2 = Slider(
                slider2_pos, 'th2', -1.0*math.pi, 1.0*math.pi, 0.0*math.pi)
            threshold_slider2.on_changed(update_th2)

            slider3_pos = plt.axes([0.1, 0.05, 0.8, 0.03])
            threshold_slider3 = Slider(
                slider3_pos, 'th3', -1.0*math.pi, 1.0*math.pi, 0.0*math.pi)
            threshold_slider3.on_changed(update_th3)

        graph.set_linestyle('-')
        graph.set_linewidth(5)
        graph.set_marker('o')
        graph.set_markerfacecolor('g')
        graph.set_markeredgecolor('g')
        graph.set_markersize(15)
        plt.grid()
        plt.show()
