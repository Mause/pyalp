from django import template

register = template.Library()

from pyalp_page.module_node import ModuleNode


class StartModuleNode(ModuleNode):
    template_name = 'start_module.html'


register.tag('start_module', StartModuleNode.invoke)
