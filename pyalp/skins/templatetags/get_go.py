from os.path import join

from django import template
from common.generic_template_tag import GenericTemplateTag


class GetGoNode(GenericTemplateTag):
    template = 'get_go.html',

    def __init__(self, url):
        self.url = url

    def render(self, context):
        skin = context['skin']
        tempurl = skin.images['go']

        width, height = skin.getimagesize(
            join(skin.asset_path, tempurl)
        )

        return self.render_to_string({
            'url': self.url,
            'tempurl': tempurl,
            'width': width,
            'height': height
        })

register = template.Library()
register.tag('get_go', GetGoNode.invoke)
