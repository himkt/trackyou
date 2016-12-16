# -*- coding: utf-8 -*-
from pypandoc import convert_file
from re import sub
from datetime import datetime

from .modules.plotter import Plotter

class TrackYou(object):
    def __init__(self, target: str, title: str, output_dir: str, plot_feature: bool = False):
        self.target = target
        self.title = title
        self.output_dir = output_dir
        self.plot_feature = plot_feature

        if plot_feature:
            self.trackyou_plt = Plotter(output_dir + title + '.tsv')

    def report(self):
        print(self.output_dir + self.title + '.tsv')

        with open(self.output_dir + self.title + '.tsv', 'a') as f:
            print(self._daystring(), self._count(), sep='\t', file=f)

        if self.plot_feature:
            self.trackyou_plt.run_server()

    def _count(self):
        document = convert_file(self.target, 'plain')
        document = sub(r'\n|\-|\s|=', '', document)
        return len(document)

    def _daystring(self):
        return str(datetime.today()).split()[0]
