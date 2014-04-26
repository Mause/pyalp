
from django import template

from pyalp_page.template_render_node import TemplateRenderNode

register = template.Library()


class DisplayTopNode(TemplateRenderNode):
    template_name = '_top.html'


@register.tag
def display_top(parser, token):
    return DisplayTopNode()
