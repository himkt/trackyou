import unittest

from trackyou.trackyou import TrackYou


class MyTestCase(unittest.TestCase):

    def test_report(self):
        ty = TrackYou(target='dat/test.tex', title='test', output_dir='dat/')
        ty.report()

    def test_report_with_plot(self):
        ty = TrackYou(target='dat/test.tex', title='test',
                      output_dir='dat/', plot_feature=True)
        ty.report()


if __name__ == '__main__':
    unittest.main()
