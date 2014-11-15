import numpy as np
from bokeh.plotting import *
from bokeh.models import BoxSelectTool
N = 100

x = np.linspace(0, 4*np.pi, N)
y = np.sin(x)

output_file("scatter_selection.html", title="scatter_selection.py example")

figure(tools="pan,wheel_zoom,box_zoom,reset,previewsave,select")

l = scatter(x,y,
    color="red",
    title="select on mouseup"
)
select_tool = curplot().select(dict(type=BoxSelectTool))
select_tool.select_every_mousemove = False

l = scatter(x,y,
    marker="square", color="green",
    title='select on mousemove'
    )
select_tool = curplot().select(dict(type=BoxSelectTool))

scatter(x,y,
    color="#FF00FF", nonselection_fill_color="#FFFF00", nonselection_fill_alpha=1
)

select_tool.select_every_mousemove = True

scatter(x,y,
    marker="square", color="blue", name="scatter_selection_example"
)

show()  # open a browser
