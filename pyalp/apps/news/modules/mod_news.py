from django.template.loader import render_to_string

from news.models import NewsItem
from modules.module_utils import ModuleLibrary


register = ModuleLibrary()


@register.module
class NewsModule(object):
    module_name = 'mod_news'

    def render(self, context):
        news = NewsItem.objects.filter(hide_item=False).order_by('itemtime')
        # $news = $dbc->database_query("SELECT * FROM news WHERE hide_item=0
            # ORDER BY itemtime DESC");

        return render_to_string(
            'mod_news.html',
            {'news': news},
            context_instance=context
        )
