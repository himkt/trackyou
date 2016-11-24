# trackyou

How many words did you write today ?

# Requirement

You have to install [pandoc](http://pandoc.org/)

If you have already installed [homebrew](http://brew.sh/), you can install pandoc with

> brew install pandoc

# installation

> pip install trackyou


# Run

```python
from trackyou.trackyou import TrackYou

ty = TrackYou(target=prefix + 'path_to_tex', title='hoge', output_dir=prefix + 'dir_output' + '/')
ty.report()
````
