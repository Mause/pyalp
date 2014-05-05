# from os.path import join

from django import template

from common.generic_template_tag import GenericTemplateTag


class DottedLineNode(GenericTemplateTag):
    template = 'dotted_line.html'

    def __init__(self, toppadding=4, botpadding=0, width='100%'):
        self.toppadding = toppadding
        self.botpadding = botpadding
        self.width = width

    def render(self, context):
        return self.render_to_string({
            'toppadding': self.toppadding,
            'botpadding': self.botpadding,
            'width': self.width
        }, context_instance=context)


register = template.Library()
register.tag('dotted_line', DottedLineNode.invoke)
