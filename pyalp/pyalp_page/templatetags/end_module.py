from django import template


from pyalp_page.module_node import ModuleNode


class EndModuleNode(ModuleNode):
    template_name = 'end_module.html'

    def __init__(self, module_type="main", bgcolor=""):
        super().__init__(module_type=module_type, bgcolor=bgcolor)


register = template.Library()
register.tag('end_module', EndModuleNode.invoke)
