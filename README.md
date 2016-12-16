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
```


# Run with plot

Thanks to this [Pull Request](https://github.com/himkt/trackyou/pull/1), trackyou can provide graphical interface for visualize your progress (__To enable this feature, you have to install bottle__) !

If you wanna enable this feature, you have to install [bottle](http://bottlepy.org/docs/dev/)

```python
from trackyou.trackyou import TrackYou

ty = TrackYou(target=prefix + 'path_to_tex', title='hoge', output_dir=prefix + 'dir_output' + '/', plot_feature=True)
ty.report()
```
