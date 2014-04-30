import importlib

from django import template
from django.utils.text import unescape_string_literal

from pyalp_translation.customization import GetTexter

register = template.Library()


class TransNode(template.Node):
    def __init__(self, s):
        self.s = s

    def get_app(self, context):
        app_name = context['app_name']
        assert app_name, (
            "Did you make sure to set the context_instance "
            "to and instance of RequestContext"
        )
        return importlib.__import__(app_name)

    def render(self, context):
        if 'page_context' in context:
            return GetTexter(context['page_context'])(self.s)
        else:
            return self.try_with_custom(context)

    def try_with_custom(self, context):
        app = self.get_app(context)

        try:
            custom_gettext = getattr(app, 'gettext')
        except AttributeError:
            # if no custom gettext is supplied for the app,
            # assume global
            return GetTexter('global')(self.s)
        else:
            return custom_gettext(self.s)


def trans_standalone(context, s):
    return TransNode(s).render(context)


def get_const_name(token):
    try:
        # split_contents() knows not to split quoted strings.
        tag_name, arg = token.split_contents()
    except ValueError:
        token = token.contents.split()[0]
        raise template.TemplateSyntaxError(
            "{} tag requires a single argument".format(token)
        )

    return unescape_string_literal(arg)


@register.tag
def trans(parser, token):
    """
    Used to interact with pyalp's custom translation implementation

    Usage:

    .. code-block::

        {% trans "key" %}

    """
    const_name = get_const_name(token)

    return TransNode(const_name)
