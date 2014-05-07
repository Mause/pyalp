from django import template
from django.template.loader import render_to_string


def split_into_variables(token):
    # split and remove name
    tokens = token.split_contents()[1:]
    return map(template.Variable, tokens)


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
        variables = split_into_variables(token)

        try:
            return cls(*variables)
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
