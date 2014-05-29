from common.generic_template_tag import GenericTemplateTag


COLOURS = [
    '009999', '3333cc', '009900', '66cc00',
    '99cc00', 'ffff00', 'ffcc00',
    'ff6600', 'ff0000', '990000'
]


class SeverityColourNode(GenericTemplateTag):
    def __init__(self, severity):
        self.severity = severity

    def render(self, context):
        severity = self.resolve(context, self.severity)

        severity = (severity * 2) - 1

        return COLOURS[severity]


from django.template import Library
register = Library()
register.tag('severity_colour', SeverityColourNode.invoke)
