from ..models import Tournament
from django.template.loader import render_to_string

from modules.module_utils import ModuleLibrary
register = ModuleLibrary()

@register.module
class ModTournaments(object):
    module_name = 'mod_tournaments'

    def __init__(self):
        pass

    def render(self, context):
        # global $dbc, $colors, $master, $toggle, $userinfo, $images;
        flags = context['flags']
        skin = context['skin']

        # SELECT tourneyid, name, marathon, lockstart
        # FROM tournaments
        # WHERE tentative=0
        # ORDER BY name

        data = Tournament.objects.filter(tentative=False).order_by('name')

        # 'SELECT username FROM users WHERE userid='.master['marathonleader']

        return render_to_string(
            'mod_tournaments.html',
            {'data': data},
            context_instance=context
        )
