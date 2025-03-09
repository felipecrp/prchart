from abc import abstractmethod
import matplotlib.pyplot as plt

from prplot.style.chart_style import ChartStyle


class Plot:
    def __init__(self):
        self.chart = None
        self.fig = None
        self.ax = None

    @property
    def data(self):
        return self.chart.data
    
    @property
    def style(self) -> ChartStyle:
        return self.chart.style

    @abstractmethod
    def draw(self):
        pass

    def show(self):
        if not self.ax:
            self.draw()
        plt.show()
        return self

    def save(self, filename):
        if not self.ax:
            self.draw()
        self.fig.savefig(filename)
        return self


class Bar(Plot):
    def draw(self):
        self.fig, self.ax = plt.subplots()
        ax = self.ax

        category_name = self.chart.binds['category']
        categories = self.chart.data.groupby([category_name]).size().reset_index(name='count')

        cat = categories[category_name]
        counts = categories['count']

        ax.set_xlabel(category_name)
        ax.set_ylabel('Count')

        self.style.apply_to_axes(ax)

        ax.bar(
            cat, 
            counts, 
            color=self.style.get_color()
        )


class Scatter(Plot):
    def draw(self):
        self.fig, self.ax = plt.subplots()
        ax = self.ax

        x_name = self.chart.binds['x'] 
        y_name = self.chart.binds['y']

        x = self.chart.data[x_name]
        y = self.chart.data[y_name]

        ax.set_xlabel(x_name)
        ax.set_ylabel(y_name)

        self.style.apply_to_axes(ax)

        ax.scatter(
            x, 
            y,
            color=self.style.get_color()
        )


class BoxPlot(Plot):
    def draw(self):
        self.fig, self.ax = plt.subplots()
        ax = self.ax

        x_name = self.chart.binds['x']
        y_name = self.chart.binds['y']

        categories = self.data.groupby([x_name])[y_name].apply(list)
        tick_labels = list(categories.index)

        ax.set_xlabel(x_name)
        ax.set_ylabel(y_name)
        
        self.style.apply_to_axes(ax)

        ax.boxplot(
            categories,
            tick_labels = tick_labels,
            # color = self.style.get_color()
        )
