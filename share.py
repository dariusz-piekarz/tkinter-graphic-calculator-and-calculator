# class share allow communication and share data with other classes that constitutes different element of the
# application.for instance choice of style is stored in the class and class Draw (so is the Frame1)
# can access to plot style  data.
class Share:

    help_counter = 0
    plot_style = dict({'bg_plot_color': "", 'ax_plot_color': "", 'line_plot_color': "", 'line_thickness': 1})
    window_width = 0.0
    window_height = 0.0
    total_width = 0.0
    total_height = 0.0

# the author: Dariusz Piekarz
