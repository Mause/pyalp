from django import template
from django.template.loader import render_to_string
from common.generic_template_tag import GenericTemplateTag

from cl_module.models import Module

register = template.Library()


class IndexModulesNode(GenericTemplateTag):
    def __init__(self, side=1):
        self.side = side

    def render(self, context):
        modules = Module.objects.filter(enabled=True)
        modules = modules.order_by('ordernum')

        from operator import attrgetter
        names = map(attrgetter('name'), modules)
        print('index modules:', ', '.join(names))

        half_modules = []
        for mod in modules:
            # req = mod.required
            # if hasattr(get_flag_registry(), req):
            half_modules.append(mod)

        return render_to_string(
            'index_modules.html',
            {'half_modules': half_modules},
            context_instance=context
        )


register.tag('index_modules', IndexModulesNode.invoke)
