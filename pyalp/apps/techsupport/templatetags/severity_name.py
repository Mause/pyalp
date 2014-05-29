from common.generic_template_tag import GenericTemplateTag


SEVERITY_NAMES = {
    1: "1 [annoying]",
    2: "2 [minor]",
    3: "3 [important]",
    4: "4 [major]",
    5: "5 [critical]"
}


class SeverityNameNode(GenericTemplateTag):
    def __init__(self, severity):
        self.severity = severity

    def render(self, context):
        severity = self.resolve(context, self.severity)
        return SEVERITY_NAMES.get(severity)


from django.template import Library
register = Library()
register.tag('severity_name', SeverityNameNode.invoke)
