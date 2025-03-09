import matplotlib.pyplot as plt


class Plot:
    def __init__(self):
        self.chart = None

    @property
    def data(self):
        return self.chart.data

    def save(self, filename):
        pass


class Bar(Plot):
    def show(self):
        fig, ax = plt.subplots()

        category_name = self.chart.binds['category']
        categories = self.chart.data.groupby([category_name]).size().reset_index(name='count')

        cat = categories[category_name]
        counts = categories['count']

        ax.set_xlabel(category_name)
        ax.set_ylabel('Count')

        ax.bar(cat, counts)
        # ax.bar(cat, counts, label=bar_labels, color=bar_colors)

        plt.show()
        print('bar plot')


class Scatter(Plot):
    def show(self):
        fig, ax = plt.subplots()

        x_name = self.chart.binds['x'] 
        y_name = self.chart.binds['y']

        x = self.chart.data[x_name]
        y = self.chart.data[y_name]

        ax.set_xlabel(x_name)
        ax.set_ylabel(y_name)

        ax.scatter(x, y)

        plt.show()
        print('scatter plot')


class BoxPlot(Plot):
    def show(self):
        fig, ax = plt.subplots()

        x_name = self.chart.binds['x']
        y_name = self.chart.binds['y']

        categories = self.data.groupby([x_name])[y_name].apply(list)
        tick_labels = list(categories.index)

        ax.set_xlabel(x_name)
        ax.set_ylabel(y_name)

        ax.boxplot(
            categories,
            tick_labels = tick_labels,
        )

        plt.show()
        print('box plot')
