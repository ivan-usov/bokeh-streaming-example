from bokeh.io import curdoc
from bokeh.plotting import ColumnDataSource, figure

import receiver

FPS = 1

doc = curdoc()
source = ColumnDataSource({'x': [], 'y': []})

f = figure()
l = f.line(x='x', y='y', source=source)

def update():
    if receiver.buffer:
        data = receiver.buffer[-1]
        source.data.update(x=range(len(data)), y=data)

doc.add_periodic_callback(update, 1000/FPS)
doc.add_root(f)
