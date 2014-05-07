import importlib

from django import template

from pyalp_translation.customization import GetTexter
from common.generic_template_tag import GenericTemplateTag

register = template.Library()


class TransNode(GenericTemplateTag):
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
        self.s = self.resolve(context, self.s)
        assert not hasattr(self.s, 'resolve')

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


@register.tag
def trans(parser, token):
    """
    Used to interact with pyalp's custom translation implementation

    Usage:

    .. code-block::

        {% trans "key" %}

    """

    return TransNode.invoke(parser, token)
