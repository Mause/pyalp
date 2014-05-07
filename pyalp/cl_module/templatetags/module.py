from django import template

register = template.Library()


from os.path import exists, join
from django.template.loader import render_to_string
from django.contrib.staticfiles.storage import staticfiles_storage

from common.generic_template_tag import (
    GenericTemplateTag,
    split_into_variables
)


class ModuleNode(GenericTemplateTag):
    def __init__(self, contents, module_type='main', string='', bgcolor='',
                 link='', width='100%', align=''):
        self.contents = contents

        self.bgcolor = bgcolor
        self.string = string
        self.module_type = module_type
        self.link = link
        self.align = align

    def calc_dimensions(self, skin):
        container = skin.container

        imgs = {}
        sides = ['tl', 'tr', 'bl', 'br', 't', 'b', 'lside', 'rside']
        for side in sides:
            imgs['mod' + side] = exists(join(
                skin.asset_path, 'img', 'mod' + side + '.gif'
            ))

        dims = {}
        for key, value in imgs.items():
            if value:
                path = join('img', key + '.gif')

                width, height = skin.getimagesize(join(skin.asset_path, path))

                dims[key] = {
                    'width': width,
                    'height': height,
                    'img': path,
                    'bgcolor': skin.colors['cell_background']
                }
            else:
                dims[key] = {
                    'width': container['border_width'],
                    'height': container['border_height'],
                    'img': staticfiles_storage.url("img/pxt.gif"),
                    'bgcolor': skin.colors['border']
                }

        return dims, imgs

    def render(self, context):
        skin = context['skin']

        current_color = (
            self.bgcolor if self.bgcolor
            else skin.colors['cell_background']
        )
        rowspan = 5 if self.string else 3

        dims, imgs = self.calc_dimensions(skin)
        render_context = {
            'dims': dims,
            'imgs': imgs,
            'current_color': current_color,
            'rowspan': rowspan,
            'type': self.module_type,
            'width': "100%",
            'string': self.string,
            'link': self.link,
            'align': self.align
        }

        render_context = {
            k: self.resolve(context, v)
            for k, v in render_context.items()
        }

        render_context['module_contents'] = self.contents.render(context)

        return render_to_string(
            'module.html',
            render_context,
            context_instance=context
        )


@register.tag
def start_module(parser, token):
    nodelist = parser.parse(('end_module',))
    parser.delete_first_token()

    variables = split_into_variables(token)
    variables = list(variables)

    return ModuleNode(nodelist, *variables)
