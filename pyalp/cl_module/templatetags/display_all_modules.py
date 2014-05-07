from common.generic_template_tag import GenericTemplateTag
from django.template.loader import render_to_string
from pyalp_page.templatetags.spacer import SpacerNode


class DisplayAllModulesNode(GenericTemplateTag):
    def __init__(self, side=None):
        if side is None:
            raise Exception(
                'Side is required for a display_all_modules template tag'
            )
        else:
            self.side = side

    def render(self, context):
        # displays all the modules for a side.
        side = self.resolve(context, self.side)

        skin = context['skin']
        container = skin.container
        modules = context['modules']

        if side == 'right':
            get_modules = modules.rightModules
            width_modules = container['rightmodule']
        elif side == 'left':
            get_modules = modules.leftModules
            width_modules = container['leftmodule']
        elif side == 'main':
            get_modules = modules.mainModules
            width_modules = '100%'

        if get_modules:
            render_context = {
                'modules': get_modules,
                'width_modules': width_modules
            }

            return render_to_string(
                'display_all_modules.html',
                render_context,
                context_instance=context
            )
        elif side != 'main':
            return SpacerNode(
                skin.container['horizontalpadding']
            ).render({})
        else:
            return ''

from django import template
register = template.Library()
register.tag('display_all_modules', DisplayAllModulesNode.invoke)
