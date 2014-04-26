from os.path import join

from django import template
from django.template.loader import render_to_string

register = template.Library()


class TemplateRenderNode(template.Node):
    def __init__(self, module_type="main", bgcolor=""):
        self.module_type = module_type
        self.bgcolor = bgcolor

    def render(self, context):
        skin = context['skin']
        path = join(skin.asset_path, self.template_name)

        return render_to_string(
            path,
            context
        )
