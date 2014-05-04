from os.path import join
from django import template
from common.generic_template_tag import GenericTemplateTag


class GetArrowNode(GenericTemplateTag):
    template = 'arrow.html'

    def __init__(self, arrow_type='off'):
        self.arrow_type = arrow_type

    def render(self, context):
        skin = context['skin']
        tempurl = skin.images['arrow_' + self.arrow_type]

        width, height = skin.getimagesize(
            join(skin.asset_path, tempurl)
        )

        return self.render_to_string({
            'tempurl': tempurl,
            'width': width,
            'height': height
        })

register = template.Library()
register.tag('get_arrow', GetArrowNode.invoke)
