"""
Oirignally scoring_12.php
"""
from pyalp.utils import krsort
from ..models import Player, Team, MatchesTeam, Match, Server
from django.db.models import Sum
from collections import defaultdict


def scoring(tournament):
    """
    single elimination - 1st through 4th place
    is included into disp_tournament.php
    input: tournament.per_team and tournament.tourneyid
    output: (ids of the respective placings)
        first_id, second_id, third_id, fourth_id
    """
    if tournament.per_team == 1:
        data = Player.objects.filter(tourney=tournament).select_related('user')
    elif tournament.per_team > 1:
        data = Team.objects.filter(tourney=tournament)

    scores = defaultdict(defaultdict)
    for row in data:
        t_id = data.id if tournament.per_team > 1 else data.user.id

        survived = MatchesTeam.objects.filter(
            tourney=tournament,
            team=t_id,
        ).count() - 1
        survived = survived if survived else 0

        total_score = MatchesTeam.objects.filter(
            tourney=tournament,
            team=t_id
        ).aggregate(Sum('score'))

        scores[survived][total_score["score__sum"]].append(row)

    teamscores = []
    scores = dict(krsort(scores))
    for _3key, val in scores.items():
        val = dict(krsort(val))

        for _2key, inner_val in val.items():
            inner_val = krsort(inner_val)
            for teamid in inner_val:
                teamscores.append([teamid, _3key, _2key])

    if tournament.lockfinish:
        first_id = teamscores[0][0]
        second_id = teamscores[1][0]
        third_id = teamscores[2][0]
        fourth_id = teamscores[3][0]
    else:
        first_id, second_id, third_id, fourth_id = [None] * 4

    return {
        'teamscores': teamscores,
        'first_id': first_id,
        'second_id': second_id,
        'third_id': third_id,
        'fourth_id': fourth_id
    }


def start(tournament):
    Match.objects.filter(tourney=tournament).delete()
    MatchesTeam.objects.filter(tourney=tournament).delete()

    num_servers = Server.objects.filter(tourney=tournament).count()

    new_match = Match(
        tourney=tournament,
        rnd=1,
        mtc=1,
        server=1 if num_servers else 0
    )
    new_match.save()

    if tournament.per_team > 1:
        query = Team.objects.filter(
            tourney=tournament
        )
    else:
        query = Player.objects.filter(
            tourney=tournament
        ).select_related('user')

    MatchesTeam.objects.bulk_create(
        MatchesTeam(
            tourney=tournament,
            match=new_match,
            team=row.id if tournament.per_team > 1 else row.user.id
        )
        for row in query
    )
