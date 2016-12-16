from setuptools import setup, find_packages


setup(
    name = "trackyou",
    version = "0.0.3",
    author = 'himkt',
    author_email = 'himkt@klis.tsukuba.ac.jp',
    description = 'visualize your progress',
    url = 'https://github.com/himkt/trackyou',

    packages = find_packages(),
    test_suite = 'tests',
)
