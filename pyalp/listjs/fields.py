from listjs.widgets import ListJSGridWidget
from django.forms import fields


class ListJSField(fields.Field):
    widget = ListJSGridWidget

    def __init__(self, *args, **kwargs):
        widget_kwargs = {
            'values': None
        }
        kwargs['widget'] = self.widget(**widget_kwargs)
        super(ListJSField, self).__init__(*args, **kwargs)
