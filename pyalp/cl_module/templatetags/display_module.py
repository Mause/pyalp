from common.generic_template_tag import GenericTemplateTag


class DisplayModuleProxyNode(GenericTemplateTag):
    template = 'display_module.html'

    def __init__(self, module, overwrite=''):
        self.module = module
        self.overwrite = overwrite

    def render(self, context):
        # var = self.current_security_level() >= self.get_security()
        module = self.resolve(context, self.module)
        overwrite = self.resolve(context, self.overwrite)

        var = True
        if var:
            if overwrite:
                loc = overwrite
            else:
                # if self.get_type() != "":
                #     loc = self.get_type()
                # else:
                    loc = module.loc

            render_context = {
                'loc': loc,
                'module_type': module.module_type,
                'name': module.name,
                'module': module,
                'string': module.string,
                'link': module.link
            }

            return self.render_to_string(
                render_context,
                context_instance=context
            )
        else:
            return ''

from django import template
register = template.Library()
register.tag('display_module', DisplayModuleProxyNode.invoke)
