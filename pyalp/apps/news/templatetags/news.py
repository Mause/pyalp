
from ..models import NewsItem

from common.generic_template_tag import GenericTemplateTag


class NewsNode(GenericTemplateTag):
    template = 'news.html'

    def __init__(self, all_news_items=False):
        self.all_news_items = all_news_items

    def render(self, context):
        query = NewsItem.objects.exclude(hide_item=True).order_by('itemtime')

        if self.resolve(context, self.all_news_items):
            query = query[:5]

        return self.render_to_string(
            {
                'query': query,
                'more_than_five': len(query) > 5
            },
            context_instance=context
        )

from django import template
register = template.Library()
register.tag('news', NewsNode.invoke)
