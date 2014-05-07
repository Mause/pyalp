from django.template.loader import render_to_string
from pyalp.skin import get_skin


class Bargraph(object):
    def __init__(
            self, percent, width, widthpercent,
            toppadding=6, bottompadding=4):
        # percent graph is filled.
        self.percent = percent

        # total width of the graph (in pixels, unless widthpercent is 1)
        self.width = width
        self.height = 12

        # boolean to indicate if the width variable is a percent
        self.widthpercent = widthpercent

        self.toppadding = toppadding
        self.bottompadding = bottompadding

        self.border = 1                   # border size (in pixels)

        # left or right - controls which side the filled comes from.
        self.alignment = 'left'

        # boolean to indicate if display % label on the graph
        self.labels = 1

        # whether to use the 3d background for the empty section
        self.background = True

    def render(self):
        skin = get_skin()

        render_context = {
            'bordercolor': skin.colors['border_alternate'],
            'filledcolor': skin.colors['graphs'],
            'emptycolor': skin.colors['cell_title'],
            'labelfilledcolor': skin.colors['cell_background'],
            'labelemptycolor': skin.colors['text'],
            'emptybg': skin.images['empty_bargraph_background'],

            'toppadding': self.toppadding,
            'bottompadding': self.bottompadding,
            'width': self.width,
            'height': self.height,
            'alignment': self.alignment,
            'border': self.border,
            'background': self.background,

            'display_percentage': round(self.percent * 100),
            'width_middlepart': '{}%'.format(round(
                self.width - self.percent *
                self.width
            )),
            'width_firstpart': '{}%'.format(round(
                self.percent *
                self.width
            )),
            'widthpercent': '%' if self.widthpercent else ''
        }

        return render_to_string('cl_bargraph.html', render_context)
