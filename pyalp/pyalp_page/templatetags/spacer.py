# from os.path import join

from django import template
from django.template.loader import render_to_string

from common.generic_template_tag import GenericTemplateTag


class SpacerNode(GenericTemplateTag):
    template = 'spacer.html'

    def __init__(self, width=1, height=1, br=False, align=''):
        self.width = width
        self.height = height
        self.br = br
        self.align = align

    @classmethod
    def init_lit(self, width=1, height=1, br=False, align='""'):
        import pudb
        pudb.set_trace()
        width = template.Variable(str(width))
        height = template.Variable(str(width))
        br = template.Variable(str(br))
        align = template.Variable(str(align))

        return SpacerNode(width, height, br, align)

    def render(self, context):
        "returns a width x height pixel image."

        cur_context = {
            'width': self.width,
            'height': self.height,
            'br': self.br,
            'align': self.align
        }

        cur_context = {
            k: v.resolve(context)
            for k, v in cur_context.items()
        }

        return render_to_string(
            'spacer.html',
            cur_context,
            context_instance=context
        )




register = template.Library()
register.tag('spacer', SpacerNode.invoke)
