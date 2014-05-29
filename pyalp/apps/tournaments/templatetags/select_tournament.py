from common.generic_template_tag import GenericTemplateTag
from ..models import Tournament


class SelectTournamentNode(GenericTemplateTag):
    template = 'select_tournament.html'

    def __init__(self, started=''):
        self.started = started

    def render(self, context):
        data = Tournament.objects.order_by('name')

        started = self.resolve(context, self.started)
        if started != '':
            data = data.filter(lockstart=started)

        return self.render_to_string(
            {'data': data},
            context_instance=context
        )


from django.template import Library
register = Library()
register.tag('select_tournament', SelectTournamentNode.invoke)
