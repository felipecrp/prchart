from .chart_style import ChartStyle


class Grayscale(ChartStyle):
    def __init__(self):
        super().__init__(dict(
            axes = dict(
                left = dict(
                    spine = dict(
                        color = '#333',
                    ),
                    label = dict(
                        color = '#333',
                        fontsize = 10,
                        fontweight = 'normal',
                        fontname = 'FreeSans'
                    ),
                    tick = dict(
                        color = '#333',
                        fontsize = 10,
                        rotation = 0,
                    ),
                ),
                top = dict(
                    spine = dict(
                        color = '#333'
                    ),
                ),
                right = dict(
                    spine = dict(
                        color = '#333'
                    ),
                ),
                bottom = dict(
                    spine = dict(
                        color = '#333',
                    ),
                    label = dict(
                        color = '#333',
                        fontsize = 10,
                        fontweight = 'normal',
                        fontname = 'FreeSans'
                    ),
                    tick = dict(
                        color = '#333',
                        fontsize = 10,
                        rotation = 0,
                    ),
                ),  

            )
        ))

    def get_color(self):
        return '#333'

        