from os.path import exists
from django import template
from django.template.loader import render_to_string


class ModuleNode(template.Node):
    def __init__(self, type='main', string='', bgcolor='', link='',
                 width='100%', align=''):
        self.bgcolor = bgcolor
        self.string = string

    def calc_dimensions(self, skin):
        container = skin.container

        imgs = {}
        sides = ['tl', 'tr', 'bl', 'br', 't', 'b', 'lside', 'rside']
        for side in sides:
            imgs['mod' + side] = exists(
                skin.asset_path + 'mod' + side + '.gif'
            )

        dims = {}
        for key, value in imgs.items():
            if value:
                width, height = skin.getimagesize(
                    skin.asset_path + key + '.gif')
                dims[key] = {
                    'width': width,
                    'height': height,
                    'img': skin.asset_path + key,
                    'bgcolor': skin.colors['cell_background']
                }
            else:
                dims[key] = {
                    'width': container['border_width'],
                    'height': container['border_height'],
                    'img': "img/pxt.gif",
                    'bgcolor': skin.colors['border']
                }

        return dims

    def render(self, context):
        # global lan, colors, master, container;
        skin = context['skin']

        current_color = (
            self.bgcolor if self.bgcolor
            else skin.colors['cell_background']
        )
        rowspan = 5 if self.string else 3

        render_context = {
            'dims': self.calc_dimensions(skin),
            'current_color': current_color,
            'rowspan': rowspan,
            'width': 500
        }

        return render_to_string(
            self.template_name,
            render_context,
            context_instance=context
        )
