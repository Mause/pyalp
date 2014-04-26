from django import template

from pyalp_page.template_render_node import TemplateRenderNode

register = template.Library()


class DisplayBottomNode(TemplateRenderNode):
    template_name = '_bot.html'

    def render(self, context):
        skin = context['skin']

        if 'image_text' in skin.colors:
            color = skin.colors['image_text']
        else:
            color = 'white'
        context['copyright_img_src'] = 'img/{}_copyright.gif'.format(color)
        context['license_img_src'] = 'img/{}_license.gif'.format(color)

        return super().render(context)


@register.tag
def display_bottom(parser, token):
    return DisplayBottomNode()
