# -*- coding: utf-8 -*-
import csv

from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

import webbrowser as web
from matplotlib import style

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
                timestamp, num_words = row
                trackyou_data[timestamp] = int(num_words)

    @route("/plot")
    def plot():
        x = []
        y = []

        for i, timestamp in enumerate(sorted(trackyou_data.keys())):
            y.append(trackyou_data[timestamp])
            x.append(timestamp)

        style.use('ggplot')
        fig = Figure()
        canvas = FigureCanvas(fig)
        ax = fig.add_subplot(211)
        ax.plot(y)

        # ax.fill_between(x, y, color="skyblue", alpha=0.3) TODO
        # ax.set_xticklabels(x) # TODO: FigureCanvas show fixed labels
        # ax.set_xlabel('date')
        ax.set_xticklabels([])
        ax.set_title('How many words did you write today ?')
        ax.grid(True)
        ax.set_ylabel('count')
        canvas.print_figure("tmp.png")
        return static_file("tmp.png", root='./', mimetype='image/png')

    def run_server(self):
        self.set_data()
        web.open(self.plot_url)
        run(host="localhost", port="7979")
