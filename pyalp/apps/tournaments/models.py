from django.db import models


class Tournament(models.Model):
    pass


class Game(models.Model):
    pass


class PollMaps(models.Model):
    pass


class Moderator(models.Model):
    pass


class TournamentMatchesTeams(models.Model):
    # i presume this is to resolve the many to many between Tournament's
    # and Matches and Teams
    pass
