from pypandoc import convert_file
from re import sub
from datetime import datetime

class TrackYou(object):
    def __init__(self, target: str, title: str, output_dir: str):
        self.target = target
        self.title = title
        self.output_dir = output_dir

    def report(self):
        print(self.output_dir + self.title + '.tsv')

        with open(self.output_dir + self.title + '.tsv', 'a') as f:
            print(self._daystring(), self._count(), sep='\t', file=f)

    def _count(self):
        document = convert_file(self.target, 'plain')
        document = sub(r'\n|\-|\s|=', '', document)
        return len(document)

    def _daystring(self):
        return str(datetime.today()).split()[0]