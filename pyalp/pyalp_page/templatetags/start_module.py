from django import template

register = template.Library()

from pyalp_page.module_node import ModuleNode


class StartModuleNode(ModuleNode):
    template_name = 'start_module.html'


@register.tag
def start_module(parser, token):
    return StartModuleNode()
