from django import template
import pudb

register = template.Library()


class DebuggerNode(template.Node):
    def render(self, context):
        pudb.set_trace()
        return ""


@register.tag
def debugger(parser, token):
    """
    Activates a debugger session in both passes of the template renderer
    """
    pudb.set_trace()

    return DebuggerNode()
