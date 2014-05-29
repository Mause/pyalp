from django.db import models
from django.conf import settings

# Create your models here.


class Song(models.Model):
    """
    "music" => "musicid int(11) NOT NULL auto_increment,
        title varchar(64) NOT NULL default '',
        artist varchar(64) NOT NULL default '',
        genre varchar(40) NOT NULL default '',
        path TEXT NOT NULL default '',
        plays int(4) NOT NULL default '0',
        playingid int(11) unsigned NOT NULL default '0',
        nowplaying tinyint(1) NOT NULL default '0',
        votes int(11) unsigned NOT NULL default '0',
        PRIMARY KEY  (musicid)",
    """

    # title varchar(64) NOT NULL default '',
    title = models.CharField(max_length=64)

    # artist varchar(64) NOT NULL default '',
    artist = models.CharField(max_length=64)

    # genre varchar(40) NOT NULL default '',
    genre = models.CharField(max_length=40)

    # path TEXT NOT NULL default '',
    path = models.TextField()

    # plays int(4) NOT NULL default '0',
    plays = models.IntegerField()

    # playingid int(11) unsigned NOT NULL default '0',
    # person who originally added song
    playing = models.ForeignKey(settings.AUTH_USER_MODEL)

    # nowplaying tinyint(1) NOT NULL default '0',
    nowplaying = models.BooleanField()

    # votes int(11) unsigned NOT NULL default '0',
    votes = models.IntegerField()

    def __str__(self):
        return '{} by {}'.format(
            self.title,
            self.artist
        )


class Vote(models.Model):
    """
    "music_votes" => "voteid int(11) unsigned NOT NULL auto_increment,
        playingid int(11) unsigned NOT NULL default '0',
        musicid int(11) unsigned NOT NULL default '0',
        userid int(11) unsigned NOT NULL default '0',
        subtime int(12) NOT NULL default '0',
        PRIMARY KEY  (voteid)",
    """

    # playingid int(11) unsigned NOT NULL default '0',
    # ??????

    # musicid int(11) unsigned NOT NULL default '0',
    music = models.ForeignKey(Song)

    # userid int(11) unsigned NOT NULL default '0',
    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    # subtime int(12) NOT NULL default '0',
