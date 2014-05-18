from django.conf import settings
from vanilla import CreateView

from pyalp.utils import render_to_response
from tournaments.models import (
    Tournament,
    PollMaps,
    TournamentMatchesTeams
)


get_what_teams_called = lambda: None
get_num_teams = lambda: None
make_tournament_link = lambda: None


def allscores(tournament, team):
    # SELECT score FROM tournament_matches_teams WHERE
    # tourneyid='".tournament.id."' AND team='".teamid."'");

    query = TournamentMatchesTeams.objects.filter(
        tourney=tournament, team=team
    )
    return sum(query.values_list('score', flat=True))


class TournamentsView(CreateView):
    def get(self, request):
        context = {}

        tournament_id = request.GET.get('id', False)
        if tournament_id:
            tournament = Tournament.objects.filter(tournament_id).one()

            # tournament = 'SELECT tourneyid, ttype, tournaments.*
            # FROM tournaments WHERE tourneyid='.(int)_GET['id']);
            context['game'] = tournament.game

            context['txt'] = get_what_teams_called(tournament.id)

            team_num = get_num_teams(tournament.id)
            if tournament.lockstart:
                link = make_tournament_link(tournament.id)
            else:
                link = 'disp_teams.php?id=' + tournament.id

            polls = PollMaps.objects.filter(tourney=tournament, selected=True)
            if not settings.ALP_TOURNAMENT_MODE and polls.count():
                mapvote = True
            else:
                mapvote = False

            top_four = polls.fetch(4).ids

        context = {
            'team_num': team_num,
            'top_four': top_four,
            'link': link,
            'mapvote': mapvote
        }

        return render_to_response(
            'tournaments_get.html',
            context,
            request
        )

    def post(self):
        return render_to_response('tournaments_post.html')
