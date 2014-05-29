from common.generic_template_tag import GenericTemplateTag
from ..utils import get_what_teams_called, make_tournament_link

from ..models import PollMap


class DisplayTournamentMenuNode(GenericTemplateTag):
    template = 'display_tournament_menu.html'

    def __init__(self, tourney, double_br=1, extra_admin=0):
        self.tourney = tourney
        self.double_br = double_br
        self.extra_admin = extra_admin

    def render(self, context):
        tourney = self.resolve(context, self.tourney)

        txt = get_what_teams_called(tourney);
        link = make_tournament_link(tourney);

        mapvote = PollMap.objects.filter(tourney=tourney, selected=True)
        render_context = {
            'txt': txt,
            'link': link,
            'mapvote': mapvote,
            'double_br': self.resolve(context, self.double_br),
            'extra_admin': self.resolve(context, self.extra_admin),
            'tourney': tourney
        }

        return self.render_to_string(
            render_context,
            context_instance=context
        )



from django.template import Library
register = Library()
register.tag('display_tournament_menu', DisplayTournamentMenuNode.invoke)
