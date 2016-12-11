# -*- coding: utf-8 -*-
import csv
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import webbrowser as web

from bottle import route
from bottle import run
from bottle import static_file

trackyou_data = {}
class Plotter(object):
    """ Visualization of progress class. """

    def __init__(self, target_path):
        self.target_path = target_path
        self.plot_url = "http://localhost:7979/plot"

    def set_data(self):
        with open(self.target_path) as f:
            reader = csv.reader(f, delimiter="\t")
            for row in reader:
                k = row[0].split("-")
                if k[2] in trackyou_data:
                    trackyou_data[k[2]] = int(trackyou_data[k[2]]) + int(row[1])
                else:
                    trackyou_data[k[2]] = int(row[1])

    @route("/plot")
    def plot():
        x = []
        y = []
        for k in sorted(trackyou_data.keys()):
            y.append(trackyou_data[k])
            x.append(int(k))

        fig = Figure()
        canvas = FigureCanvas(fig)
        ax = fig.add_subplot(211)
        ax.plot(x, y)
        ax.fill_between(x,y,color="skyblue",alpha=0.3)
        ax.set_title('How many words did you write today ?')
        ax.grid(True)
        ax.set_xlabel('date')
        ax.set_ylabel('count')
        canvas.print_figure("tmp.png")
        return static_file("tmp.png", root='./', mimetype='image/png')

    def run_server(self):
        self.set_data()
        web.open(self.plot_url)
        run(host="localhost", port="7979")
