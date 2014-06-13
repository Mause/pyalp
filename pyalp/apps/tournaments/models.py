import math

from django.db import models
from django.conf import settings


class Match(models.Model):
    class Meta:
        verbose_name_plural = 'matches'
    """
    "tournament_matches" => "id BIGINT NOT NULL auto_increment,
        tourneyid BIGINT NOT NULL,
        rnd int(10) NOT NULL,
        mtc int(10) NOT NULL,
        server BIGINT NOT NULL,
        top_x_advance BIGINT NOT NULL,
        bracket varchar(3) NOT NULL,
        map varchar(120) NULL,
        id_win BIGINT NOT NULL,
        id_win_top BOOL DEFAULT '0',
        id_lose BIGINT NOT NULL,
        id_lose_top BOOL DEFAULT '0',
        PRIMARY KEY (id)",
    """

    # tourneyid BIGINT NOT NULL,
    tourney = models.ForeignKey('Tournament')

    # rnd int(10) NOT NULL,
    rnd = models.IntegerField(help_text='round?')

    # mtc int(10) NOT NULL,
    mtc = models.IntegerField(help_text='match?')

    # server BIGINT NOT NULL,
    server = models.IntegerField()

    # top_x_advance BIGINT NOT NULL,
    top_x_advance = models.IntegerField(default=1)

    # bracket varchar(3) NOT NULL,
    bracket = models.CharField(max_length=3)

    # map varchar(120) NULL,
    map = models.CharField(max_length=120)

    # id_win BIGINT NOT NULL,
    # id_win_top BOOL DEFAULT '0',
    # id_lose BIGINT NOT NULL,
    # id_lose_top BOOL DEFAULT '0',

    def __str__(self):
        return 'match for {}'.format(self.tourney.name)


class MatchesScoreVote(models.Model):
    """
    "tournament_matches_score_votes" => "id BIGINT NOT NULL auto_increment,
        tourneyid BIGINT NOT NULL,
        matchid BIGINT NOT NULL,
        userid BIGINT NOT NULL,
        entry_id BIGINT NOT NULL,
        entry_val int(10) NOT NULL,
        PRIMARY KEY (id)",
    """

    # tourneyid BIGINT NOT NULL,
    tourney = models.ForeignKey('Tournament')

    # matchid BIGINT NOT NULL,
    match = models.ForeignKey('Match')

    # userid BIGINT NOT NULL,
    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    # entry_id BIGINT NOT NULL,
    entry_id = models.ForeignKey('MatchesTeam')

    # entry_val int(10) NOT NULL,
    entry_val = models.IntegerField()


class MatchesTeam(models.Model):
    """
    "tournament_matches_teams" => "id BIGINT NOT NULL auto_increment,
        tourneyid BIGINT NOT NULL,
        matchid BIGINT NOT NULL,
        team BIGINT NOT NULL,
        top BOOL NOT NULL,
        score int(20) DEFAULT NULL,
        PRIMARY KEY (id)",
    """

    # tourneyid BIGINT NOT NULL,
    tourney = models.ForeignKey('Tournament')

    # matchid BIGINT NOT NULL,
    match = models.ForeignKey('Match')

    # team BIGINT NOT NULL,
    team = models.ForeignKey('Team')

    # top BOOL NOT NULL,
    top = models.BooleanField()

    # score int(20) DEFAULT NULL,
    score = models.IntegerField(default=None)


class Tournament(models.Model):
    """
    "tournaments" => "tourneyid BIGINT NOT NULL auto_increment,
        name varchar(255) NULL,
        ttype BIGINT NOT NULL,
        itemtime datetime NULL,
        url_stats varchar(255) NULL,
        gameid BIGINT DEFAULT '0',
        random BOOL DEFAULT '0',
        per_team int(10) DEFAULT '0',
        max_teams int(15) DEFAULT '0',
        ffa BOOL DEFAULT '0',
        marathon BOOL DEFAULT '0',
        lockteams BOOL DEFAULT '0',
        lockjoin BOOL DEFAULT '0',
        lockstart BOOL DEFAULT '0',
        lockfinish BOOL DEFAULT '0',
        teamcolors BIGINT DEFAULT '0',
        playforthird BOOL DEFAULT '0',
        doublefinal BOOL DEFAULT '0',
        switchover int(4) DEFAULT '0',
        rrsplit int(4) DEFAULT '0',
        timelimit datetime NULL,
        moderatorid BIGINT DEFAULT '0',
        notes BLOB NULL,
        settings BLOB NULL,
        tentative BOOL DEFAULT '0',
        PRIMARY KEY (tourneyid)",
    """

    # name varchar(255) NULL,
    name = models.CharField(max_length=255, help_text='tournament name')

    # ttype BIGINT NOT NULL,
    # tournament type?
    tournament_type = models.ForeignKey('TournamentType')

    @property
    def ttype(self):
        return self.tournament_type

    # itemtime datetime NULL,
    itemtime = models.DateTimeField(
        help_text='date and time of tournament'
    )

    # url_stats varchar(255) NULL,
    url_stats = models.CharField(
        max_length=255,
        help_text='url to statistics for the tournament'
    )

    # gameid BIGINT DEFAULT '0',
    game = models.ForeignKey(
        'Game',
        help_text='the game for which this tournament is for'
    )

    # random BOOL DEFAULT '0',
    random = models.BooleanField(help_text='random teams?')

    # per_team int(10) DEFAULT '0',
    per_team = models.IntegerField(help_text='maximum players per team')

    # max_teams int(15) DEFAULT '0',
    max_teams = models.IntegerField(
        help_text='maximum number of teams (empty/0 = no max)'
    )

    # ffa BOOL DEFAULT '0',
    ffa = models.BooleanField(help_text='free for all? (guess)', default=False)

    # marathon BOOL DEFAULT '0',
    marathon = models.BooleanField(
        help_text='part of the global marathon tournament?',
        default=False
    )

    # lockteams BOOL DEFAULT '0',
    lockteams = models.BooleanField(
        help_text='lock team creation?', default=False
    )

    # lockjoin BOOL DEFAULT '0',
    lockjoin = models.BooleanField(
        help_text='lock team joining and quitting?', default=False
    )

    # lockstart BOOL DEFAULT '0',
    lockstart = models.BooleanField(db_index=True, default=False)

    # lockfinish BOOL DEFAULT '0',
    lockfinish = models.BooleanField(default=False)

    # teamcolors BIGINT DEFAULT '0',
    teamcolors = models.ForeignKey('TeamType', null=True)

    # playforthird BOOL DEFAULT '0',
    playforthird = models.BooleanField(
        help_text=(
            "an extra round in single elimination tournaments that "
            "determines 3rd and 4th place."
        )
    )

    # doublefinal BOOL DEFAULT '0',
    doublefinal = models.BooleanField(
        help_text=(
            'for double elimination tournaments -- if the winner of the '
            'winners bracket has to lose twice to lose the tournament.'
        ),
        default=False
    )

    # switchover int(4) DEFAULT '0',
    switchover = models.IntegerField(
        help_text="the round number for combination tournaments to switch.",
        default=False
    )

    # rrsplit int(4) DEFAULT '0',
    rrsplit = models.IntegerField(
        help_text="how many teams are in each split of the round robin.",
        default=0
    )

    # timelimit datetime NULL,
    timelimit = models.DateTimeField(
        help_text="for ladder tournaments and maybe round robin tournaments"
    )

    # moderatorid BIGINT DEFAULT '0',
    moderator = models.ForeignKey(settings.AUTH_USER_MODEL)

    # notes BLOB NULL,
    notes = models.BinaryField(help_text='tournament rules/notes')

    # settings BLOB NULL,
    settings = models.BinaryField()

    # tentative BOOL DEFAULT '0',
    tentative = models.BooleanField(
        help_text='classify as tentative?',
        default=False
    )

    def __str__(self):
        return '{} playing {}'.format(self.name, self.game.name)

    def free_slots(self):
        players = Player.objects.filter(tourney=self).count()

        if (players % self.per_team) == 0:
            return 0
        else:
            return (self.per_team - players) % self.per_team

    def teamcount(self):
        players = Player.objects.filter(tourney=self).count()
        return math.floor(players / self.per_team)


class TournamentType(models.Model):
    # not in the original version, really just cleaner
    # array( tournament name, time variable, minimum teams )
    type_num = models.IntegerField()
    name = models.CharField(max_length=200)
    time = models.IntegerField()
    minimum_teams = models.IntegerField()

    def __str__(self):
        return '{} with old id {}'.format(self.name, self.type_num)


class Team(models.Model):
    """
    "tournament_teams" => "id BIGINT NOT NULL auto_increment,
        tourneyid BIGINT NOT NULL,
        name varchar(100) NULL,
        captainid BIGINT DEFAULT '0',
        sig varchar(20) NULL,
        sigplace BOOL DEFAULT '0',
        ranking BIGINT DEFAULT '0',
        in_ladder BOOL DEFAULT '0',
        ladder_ranking int(5) DEFAULT '0',
        PRIMARY KEY (id)",
    """

    # tourneyid BIGINT NOT NULL,
    tourney = models.ForeignKey('Tournament')

    # name varchar(100) NULL,
    name = models.CharField(max_length=100)

    # captainid BIGINT DEFAULT '0',
    captain = models.ForeignKey('Player', related_name='captain')

    # sig varchar(20) NULL,
    sig = models.CharField(max_length=20)

    # sigplace BOOL DEFAULT '0',
    sigplace = models.BooleanField(default=False)

    # ranking BIGINT DEFAULT '0',
    ranking = models.IntegerField(default=0)

    # in_ladder BOOL DEFAULT '0',
    in_ladder = models.BooleanField(default=0)

    # ladder_ranking int(5) DEFAULT '0',
    ladder_ranking = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Player(models.Model):
    """
    "tournament_players" => "id BIGINT NOT NULL auto_increment,
        tourneyid BIGINT NOT NULL,
        userid BIGINT NOT NULL,
        teamid BIGINT DEFAULT '0',
        ranking BIGINT NOT NULL,
        in_ladder BOOL NOT NULL,
        ladder_ranking int(5) NOT NULL,
        PRIMARY KEY (id)",
    """

    # tourneyid BIGINT NOT NULL,
    tourney = models.ForeignKey('Tournament', null=True)

    # userid BIGINT NOT NULL,
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True)

    # teamid BIGINT DEFAULT '0',
    team = models.ForeignKey('Team', null=True, blank=True)

    # ranking BIGINT NOT NULL,
    ranking = models.IntegerField(default=0)

    # in_ladder BOOL NOT NULL,
    in_ladder = models.BooleanField()

    # ladder_ranking int(5) NOT NULL,
    ladder_ranking = models.IntegerField()

    def __str__(self):
        return '{} of {}'.format(
            self.user.username,
            self.team.name if self.team else 'no team'
        )


class TeamType(models.Model):
    """
    "tournament_teams_type" => "id BIGINT NOT NULL auto_increment,
        gameid BIGINT DEFAULT '0',
        onename varchar(100) NULL,
        onecolor varchar(10) NOT NULL,
        twoname varchar(100) NULL,
        twocolor varchar(10) NOT NULL,
        PRIMARY KEY (id)",
    """

    # gameid BIGINT DEFAULT '0',
    game = models.ForeignKey('Game')

    # onename varchar(100) NULL,
    onename = models.CharField(max_length=100, help_text='team one name')

    # onecolor varchar(10) NOT NULL,
    onecolor = models.CharField(
        max_length=10,
        help_text=(
            'color of the team - in hex [ie: #ff0000]'
            ' or in standard color name format [ie: red]'
        )
    )

    # twoname varchar(100) NULL,
    twoname = models.CharField(max_length=100, help_text='team two name')

    # twocolor varchar(10) NOT NULL,
    twocolor = models.CharField(
        max_length=10,
        help_text=(
            'color of the team - in hex [ie: #ff0000]'
            ' or in standard color name format [ie: red]'
        )
    )

    def __str__(self):
        return '{} with teams {} and {}'.format(
            self.game.name,
            self.onename,
            self.twoname
        )


class Game(models.Model):
    """
    "games" => "gameid BIGINT NOT NULL auto_increment,
        name varchar(255) NOT NULL,
        short varchar(16) NULL,
        current_version varchar(40) NULL,
        url_update varchar(255) NULL,
        url_maps varchar(255) NULL,
        thumbs_dir varchar(255) NULL,
        querystr2 varchar(20) NULL,
        PRIMARY KEY (gameid)",
    """

    # name varchar(255) NOT NULL,
    name = models.CharField(max_length=255)

    # short varchar(16) NULL,
    short = models.CharField(max_length=16)

    # current_version varchar(40) NULL,
    current_version = models.CharField(max_length=40)

    # url_update varchar(255) NULL,
    url_update = models.CharField(max_length=255)

    # url_maps varchar(255) NULL,
    url_maps = models.CharField(max_length=255)

    # thumbs_dir varchar(255) NULL,
    thumbs_dir = models.CharField(max_length=255)

    # querystr2 varchar(20) NULL,
    querystr2 = models.CharField(max_length=20)

    hlsw_supported = models.BooleanField()

    def __str__(self):
        msg = self.name
        if self.current_version:
            msg += ' ' + self.current_version

        return msg


class GameRequest(models.Model):
    """
    "game_requests" => "id BIGINT NOT NULL auto_increment,
        userid BIGINT NOT NULL,
        gameid BIGINT DEFAULT '0',
        gamename varchar(255) NULL,
        itemtime DATETIME NOT NULL,
        ipaddress varchar(255) NULL,
        queryport varchar(10) NULL,
        PRIMARY KEY (id)",
    """

    # userid BIGINT NOT NULL,
    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    # gameid BIGINT DEFAULT '0',
    game = models.ForeignKey('Game')

    # gamename varchar(255) NULL,
    gamename = models.CharField(max_length=255)

    # itemtime DATETIME NOT NULL,
    itemtime = models.DateTimeField()

    # ipaddress varchar(255) NULL,
    ipaddress = models.CharField(max_length=255)

    # queryport varchar(10) NULL,
    queryport = models.CharField(max_length=10)


class PollMap(models.Model):
    """
    "poll_maps" => "id BIGINT NOT NULL AUTO_INCREMENT,
        tourneyid BIGINT NOT NULL,
        filename varchar(255) NOT NULL,
        selected BOOL NOT NULL,
        filedesc BLOB, PRIMARY KEY(id)",
    """

    # tourneyid BIGINT NOT NULL,
    tourney = models.ForeignKey('Tournament', null=True)

    # filename varchar(255) NOT NULL,
    filename = models.CharField(max_length=255)

    # selected BOOL NOT NULL,
    selected = models.BooleanField()

    # filedesc BLOB
    filedesc = models.TextField()

    def __str__(self):
        return 'poll_map {} for {}'.format(self.filename, self.tourney.name)


class Server(models.Model):
    """
    "servers" => "id BIGINT NOT NULL auto_increment,
        tourneyid BIGINT NOT NULL,
        name varchar(100) NULL,
        ipaddress varchar(255) NULL,
        gameid BIGINT NOT NULL,
        queryport varchar(10) NOT NULL,
        PRIMARY KEY (id)",
    """

    # tourneyid BIGINT NOT NULL,
    tourney = models.ForeignKey('Tournament', null=True)

    # name varchar(100) NULL,
    name = models.CharField(max_length=100)

    # ipaddress varchar(255) NULL,
    ipaddress = models.GenericIPAddressField()

    # gameid BIGINT NOT NULL,
    game = models.ForeignKey('Game')

    # queryport varchar(10) NOT NULL,
    queryport = models.CharField(max_length=10)

    def __str__(self):
        return '{} running {} at {}:{}'.format(
            self.name,
            self.game.name,
            self.ipaddress,
            self.queryport
        )
