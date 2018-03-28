import pandas as pd
from bokeh.io import output_file, show
from bokeh.plotting import figure, ColumnDataSource
from bokeh.models import CategoricalColorMapper
from bokeh.layouts import column, row

output_file('test.html')

#plot = figure(plot_width=600, plot_height=600, tools='pan,box_zoom,reset')
#plot.square(x=[1,2,3,4], y=[2,4,6,8], size=20)
#show(plot)

data = pd.read_csv('rent_data.csv')

vis_data = ColumnDataSource(data)

color_mapper = CategoricalColorMapper(factors=['Hours at Minimum', 'Hours at National Average'],
                                      palette=['Red', 'Blue'])

plot_mini = figure(x_axis_label='State', y_axis_label='Mean', tools='pan,wheel_zoom,box_zoom,reset,hover,save', title='Rent vs. Minimum Wage')
plot_average = figure(x_axis_label='State', y_axis_label='Mean', tools='pan,wheel_zoom,box_zoom,reset,hover,save', title='Rent vs. Average Wage')

plot_mini.diamond(x='State_Name', y='Mean', source=vis_data, size=10,
             color=dict(field='State', transform=color_mapper),
             legend='State_Name')



hover = plot.select_one(HoverTool)

hover.tooltips = [()]

plot.legend.location = 'bottom_right'

plot.legend.background = 'lightgrey'

show(plot)
#FIELDNAMES = ['id', 'State_Code', 'State_Name', 'State_ab', 'County', 'City', 'Place', 'Type', 'Primary', 'Zip_Code', 'Area_Code', 'ALand', 'AWater', 'Lat', 'Lon', 'Mean', 'Median', 'Stdev', 'Samples']
