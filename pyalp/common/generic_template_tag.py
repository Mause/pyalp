from django import template
from django.template.loader import render_to_string


class GenericTemplateTag(template.Node):
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(self)

    def render(self):
        raise NotImplementedError(self)

    def resolve(self, context, obj):
        return (
            obj.resolve(context) if hasattr(obj, 'resolve')
            else obj
        )

    @classmethod
    def invoke(cls, parser, token):
        # split and remove names
        tokens = token.split_contents()[1:]
        tokens = map(template.Variable, tokens)

        try:
            return cls(*tokens)
        except TypeError as e:
            if e.args[0].startswith('__init__'):
                message = 'Bad arguments for {}: {}'.format(cls, e)
                raise TypeError(message) from e
            else:
                raise

    def render_to_string(self, *args, **kwargs):
        return render_to_string(
            self.template,
            *args, **kwargs
        )
