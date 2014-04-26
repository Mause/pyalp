"""
aka include/touraments/_tournament_functions.php
"""

from tournaments.models import Tournament, Moderator


def get_what_teams_called(tournament, plural=True):
    if tournament.per_team == 1 or (tournament.random and not tournament.lockstart):
        return 'competitor' + ('s' if plural else '')
    else:
        return 'team' + ('s' if plural else '')


def get_num_teams(tournament, random_as_competitors=1):
    q = dbc->database_query('SELECT per_team, random, lockstart FROM tournaments WHERE tourneyid='.(int)tourneyid)

    if (dbc->database_num_rows(q)) {
        tournament = dbc->database_fetch_assoc(q)
        if (tournament['per_team'] == 1 or (tournament['random'] and !tournament['lockstart'])) {
            if (tournament['per_team'] == 1 or (tournament['random'] and !tournament['lockstart'] and random_as_competitors)) {
                teams = dbc->database_num_rows(dbc->database_query('SELECT * FROM tournament_players WHERE tourneyid='.(int)tourneyid))
            else:
                teams = ceil(dbc->database_num_rows(dbc->database_query('SELECT * FROM tournament_players WHERE tourneyid='.(int)tournament['tourneyid'])) / tournament['per_team'])
        else:
            teams = dbc->database_num_rows(dbc->database_query('SELECT * FROM tournament_teams WHERE tourneyid='.(int)tourneyid))
        if teams:
            return teams
        else:
            return 0
    else:
        return 0

def is_under_max_teams(tournament):
    q = dbc->database_query('SELECT max_teams FROM tournaments WHERE tourneyid='.(int)tourneyid)
    if (dbc->database_num_rows(q)) {
        tournament = dbc->database_fetch_assoc(q)
        teams = get_num_teams(tourneyid)
        if (tournament['max_teams'] > 0) {
            return (teams < tournament['max_teams'])
        return True
    return False


def make_tournament_link(tourneyid):
    if (current_security_level() < 2 and file_exists('_tournament_'.tourneyid.'.html')) {
        return '_tournament_'.tourneyid.'.html'
    else:
        return 'disp_tournament.php?id='.tourneyid


def tournament_is_secure(request, tourney):
    moderator = tourney.moderator

    return (current_security_level() >= 2 or (current_security_level() >= 1 and moderator == request.user):

def display_tournament_menu(tourneyid, double_br=1, extra_admin=0):
    context = {
        'txt': get_what_teams_called(tourney),
        'link': make_tournament_link(tourney)
    }

    return render_to_string(
        'tournament_menu.html', context
    )
