from os.path import exists

from django import template
from django.template.loader import render_to_string

register = template.Library()

from pyalp_page.module_node import ModuleNode


class EndModuleNode(ModuleNode):
    template_name = 'end_module.html'

    def __init__(self, module_type="main", bgcolor=""):
        self.module_type = module_type
        self.bgcolor = bgcolor

    def render(self, context):
        # global colors, container, master
        skin = context['skin']

        # globalize this for multiple formats??
        if self.bgcolor:
            current_color = self.bgcolor
        else:
            current_color = skin.colors["cell_background"]

        sides = ["tl", "tr", "bl", "br", "t", "b", "lside", "rside"]
        imgs = {
            "mod" + side: exists(skin.asset_path + "mod" + side + ".gif")
            for side in sides
        }

        dims = {}
        for key, value in imgs.items():
            if value:
                width, height = skin.getimagesize(
                    skin.asset_path + key + ".gif")
            else:
                width, height = (
                    skin.container["border_width"],
                    skin.container["border_height"]
                )
            dims[key] = {
                'width': width,
                'height': height
            }

        render_context = {
            'dims': dims,
            'current_color': current_color
        }

        return render_to_string(
            'end_module.html',
            render_context,
            context_instance=context
        )


@register.tag
def end_module(parser, token):
    return EndModuleNode()
