from django.conf import settings
from django.forms import widgets
from django.template.context import Context
from django.template.loader import render_to_string, get_template_from_string
from django.utils.safestring import mark_safe


class ListJSWidget(widgets.Widget):
    class Media:
        js = ("%s%s?v=1" % (settings.STATIC_URL, "js/list.js"),)

    def __init__(
            self, values, valueNames, show_totals=False, name='summary',
            *args, **kwargs
            ):
        self.values = values
        self.name = name
        self.valueNames = valueNames
        self.show_totals = show_totals

        return super().__init__(*args, **kwargs)

    def render_totals(self, values, valueNames):
        totals = dict.fromkeys(valueNames, 0)

        for val in values:
            for k, v in val.items():
                if isinstance(v, bool):
                    totals[k] += 1
                elif isinstance(v, (int, float)):
                    totals[k] += v
                elif hasattr(v, 'amount'):
                    totals[k] += v.amount
                else:
                    pass
                    # print(k, v)
                    # totals[k] += v

        return {
            k: v
            for k, v in totals.items()
            if k in valueNames
        }

    def create_item_template(self, valueNames):
        item = []
        for name in valueNames:
            item.append('\t<td class="%(name)s">{{%(name)s}}</td>\n' % {
                'name': name
            })
        return '<tr>\n' + ''.join(item) + '</tr>'

    def render(self, name='', value='', attrs={}):
        item = self.create_item_template(self.valueNames)

        options = {
            'valueNames': self.valueNames,
            'item': item
        }

        prerender_template = get_template_from_string(
            options['item'],
            name='listjs-prerender'
        )
        contexts = map(Context, self.values)
        prerender = map(prerender_template.render, contexts)

        context = {
            'name': self.name,
            'options': options,
            'prerender': mark_safe(''.join(prerender)),
        }

        if self.show_totals:
            totals = self.render_totals(self.values, self.valueNames)
            context['footer'] = prerender_template.render(Context(totals))

        return render_to_string('list.html', context)
