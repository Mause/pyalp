from common.generic_template_tag import GenericTemplateTag
from django.template.base import get_library
from django import template


class IncludeModuleNode(GenericTemplateTag):
    def __init__(self, name):
        self.name = name

    def render(self, context):
        name = (
            self.name.resolve(context) if hasattr(self.name, 'resolve')
            else self.name
        )

        # really quite hacky, but it works
        lib = get_library(name)
        module = lib.tags[name].__self__
        return module().render(context)


register = template.Library()
register.tag('include_module', IncludeModuleNode.invoke)
