from collections import namedtuple

from django import template
from django.utils.text import unescape_string_literal

from pyalp.skin import skin
from pyalp_translation.templatetags.trans import TransNode

register = template.Library()

Link = namedtuple('Link', 'name,url')


class RelatedLinksGroupNode(template.Node):
    def __init__(self, related_links):
        self.related_links = related_links

    def render(self, context):
        html = ""

        if self.related_links:
            html += '<font class="sm"><strong>related links</strong> //<br />'

            for link in self.related_links:
                html += "&nbsp;" + skin.get_arrow()
                html += '&nbsp;<a href="{}">'.format(link.url)

                # $val[2]>2?'<strong>super </strong>':'')
                # $val[2]>1?'<strong>administrator</strong>: ':'')

                label = TransNode(link.label).render(context)
                html += '{}</a><br />'.format(label)
            html += "</font><br />"

        return html


class RelatedLinkNode(template.Node):
    def __init__(self, label, url):
        self.label = label
        self.url = url


def get_args(token):
    try:
        # split_contents() knows not to split quoted strings.
        tag_name, label, url = token.split_contents()
    except ValueError:
        token = token.contents.split()[0]
        raise template.TemplateSyntaxError(
            "{} tag requires two arguments".format(token)
        )

    return unescape_string_literal(label), unescape_string_literal(url)


@register.tag
def relatedlink(parser, token):
    label, url = get_args(token)
    return RelatedLinkNode(label, url)


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
