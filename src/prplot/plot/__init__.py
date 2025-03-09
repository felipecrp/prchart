import matplotlib.pyplot as plt


class Plot:
    def __init__(self):
        self.chart = None


class Bar(Plot):
    def show(self):
        fig, ax = plt.subplots()

        category_name = self.chart.binds['category']
        categories = self.chart.data.groupby([category_name]).count()
        categories = self.chart.data.groupby([category_name]).size().reset_index(name='count')

        cat = categories[category_name]
        counts = categories['count']
        # bar_labels = ['red', 'blue', '_red', 'orange']
        # bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange']

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

        ax.scatter(x, y)

        plt.show()
        print('scatter plot')
