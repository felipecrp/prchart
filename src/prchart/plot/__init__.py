from abc import abstractmethod
import matplotlib.axes
import matplotlib.pyplot as plt
import matplotlib

from prchart.style.chart_style import ChartStyle


class Plot:
    def __init__(self):
        self.chart = None
        self.fig = None
        self.ax: matplotlib.axes.Axes = None

    @property
    def data(self):
        return self.chart.data
    
    @property
    def style(self) -> ChartStyle:
        return self.chart.style

    @abstractmethod
    def draw(self):
        pass


class Bar(Plot):
    def draw(self):
        x_bind = self.chart.binds['x']
        data = self.chart.data.groupby([x_bind]).size().reset_index(name='count')

        x = data[x_bind]
        y = data['count']

        self.ax.bar(
            x, 
            y, 
            color=self.style.get_color()
        )


class Scatter(Plot):
    def draw(self):
        ax = self.ax

        x_bind = self.chart.binds['x'] 
        y_bind = self.chart.binds['y']

        x = self.chart.data[x_bind]
        y = self.chart.data[y_bind]

        ax.scatter(
            x, 
            y,
            color=self.style.get_color()
        )


class BoxPlot(Plot):
    def draw(self):
        ax = self.ax

        x_name = self.chart.binds['x']
        y_name = self.chart.binds['y']

        y = self.data.groupby([x_name])[y_name].apply(list)
        x = list(y.index)

        ax.boxplot(
            y,
            tick_labels = x,
            medianprops=dict(color='#333', linewidth=2),
            flierprops=dict(
                marker='o', 
                markerfacecolor='#333', 
                markeredgecolor='#333',
                markersize=2,
            ),
            boxprops=dict(color=self.style.get_color()),
            showcaps=True,
            widths = 0.6,
            # orientation='horizontal'
        )

