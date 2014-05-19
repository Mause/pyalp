from django import template
from django.template.loader import render_to_string

from pyalp.skin import get_skin

register = template.Library()


class RelatedLinksGroupNode(template.Node):
    def __init__(self, related_links):
        self.related_links = related_links
        self.skin = get_skin()

    def render(self, context):
        if self.related_links:
            return render_to_string(
                'relatedlinks.html',
                {
                    'links': self.related_links
                },
                context_instance=context
            )
        else:
            return ''


from common.generic_template_tag import GenericTemplateTag


class RelatedLinkNode(GenericTemplateTag):
    def __init__(self, label, url):
        self.label = label
        self.url = url


register.tag('relatedlink', RelatedLinkNode.invoke)


@register.tag
def relatedlinksgroup(parser, token):
    nodelist = parser.parse(('endrelatedlinksgroup',))
    parser.delete_first_token()

    actuals = []
    for node in nodelist:
        if type(node) == template.TextNode:
            pass
        elif type(node) == RelatedLinkNode:
            actuals.append(node)
        else:
            raise template.TemplateSyntaxError(
                'relatedlinksgroup blocks can only contain relatedlink '
                'tags and misc text'
            )

    return RelatedLinksGroupNode(actuals)
