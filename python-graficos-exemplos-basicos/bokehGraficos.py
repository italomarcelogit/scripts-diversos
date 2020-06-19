import bokeh
from bokeh.io import show, output_notebook, curdoc
from bokeh.plotting import figure, output_file
from bokeh.models import ColumnDataSource, Grid, LinearAxis, Plot, VBar
from bokeh.transform import factor_cmap
from bokeh.palettes import Spectral6
import numpy as np

#grafico de linha
p = figure()
type(p)
p.line(np.arange(1,6), [6,7,2,4,5], line_width=2)
show(p)

#grafico de barras
fruits = ['Apples', 'Pears', 'Nectarines', 'Plums', 'Grapes', 'Strawberries']
counts = [5, 3, 4, 2, 4, 6]

source = ColumnDataSource(data=dict(fruits=fruits, counts=counts, color=Spectral6))

p = figure(x_range=fruits, y_range=(0,np.array(counts).max()+5), plot_height=350, title="Fruit Counts",
           toolbar_location=None, tools="")

p.vbar(x='fruits', top='counts', width=0.9, color='color', legend_field="fruits", source=source)

p.xgrid.grid_line_color = None
p.legend.orientation = "horizontal"
p.legend.location = "top_center"

show(p)








