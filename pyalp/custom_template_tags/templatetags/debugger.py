from django import template
import pudb

register = template.Library()


class DebuggerNode(template.Node):
    def render(self, context):
        pudb.set_trace()
        return ""


@register.tag
def debugger(parser, token):
    pudb.set_trace()

    return DebuggerNode()
