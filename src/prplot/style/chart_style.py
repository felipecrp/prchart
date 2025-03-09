from abc import abstractmethod
import matplotlib
import matplotlib.axes._axes


class ChartStyle:
    def __init__(self, style: matplotlib.axes._axes.Axes):
        self.style = style
        
    def apply_to_axes(self, ax):
        ax.get_xaxis().get_label().set_color(self.style['axes']['bottom']['label']['color'])
        ax.get_xaxis().get_label().set_fontsize(self.style['axes']['bottom']['label']['fontsize'])
        ax.get_xaxis().get_label().set_fontweight(self.style['axes']['bottom']['label']['fontweight'])
        ax.get_xaxis().get_label().set_fontname(self.style['axes']['bottom']['label']['fontname'])
        ax.get_xaxis().set_tick_params(labelcolor=self.style['axes']['bottom']['tick']['color'])
        ax.get_xaxis().set_tick_params(labelsize=self.style['axes']['bottom']['tick']['fontsize'])
        ax.get_xaxis().set_tick_params(labelrotation=self.style['axes']['bottom']['tick']['rotation'])

        ax.get_yaxis().get_label().set_color(self.style['axes']['left']['label']['color'])
        ax.get_yaxis().get_label().set_fontsize(self.style['axes']['left']['label']['fontsize'])
        ax.get_yaxis().get_label().set_fontweight(self.style['axes']['left']['label']['fontweight'])
        ax.get_yaxis().get_label().set_fontname(self.style['axes']['left']['label']['fontname'])
        ax.get_yaxis().set_tick_params(labelcolor=self.style['axes']['left']['tick']['color'])
        ax.get_yaxis().set_tick_params(labelsize=self.style['axes']['left']['tick']['fontsize'])
        ax.get_yaxis().set_tick_params(labelrotation=self.style['axes']['left']['tick']['rotation'])

        # ax.set_facecolor("#fff")
        # ax.grid(color='#ddd', linestyle='-', linewidth=0.5)

        if self.style['axes']['left']['spine']['color']:
            ax.spines['left'].set_color(self.style['axes']['left']['spine']['color'])
        else:
            ax.spines['left'].set_visible
        if self.style['axes']['top']['spine']['color']:
            ax.spines['top'].set_color(self.style['axes']['top']['spine']['color'])
        else:
            ax.spines['top'].set_visible(False)
        if self.style['axes']['right']['spine']['color']:
            ax.spines['right'].set_color(self.style['axes']['right']['spine']['color'])
        else:        
            ax.spines['right'].set_visible(False)
        if self.style['axes']['bottom']['spine']['color']:
            ax.spines['bottom'].set_color(self.style['axes']['bottom']['spine']['color'])
        else:
            ax.spines['bottom'].set_visible(False)

    @abstractmethod
    def get_color(self):
        pass
