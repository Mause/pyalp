# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=255)),
                ('short', models.CharField(max_length=16)),
                ('current_version', models.CharField(null=True, max_length=40, blank=True)),
                ('url_update', models.CharField(null=True, max_length=255, blank=True)),
                ('url_maps', models.CharField(null=True, max_length=255, blank=True)),
                ('thumbs_dir', models.CharField(null=True, max_length=255, blank=True)),
                ('querystr2', models.CharField(max_length=20)),
                ('hlsw_supported', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GameRequest',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('gamename', models.CharField(max_length=255)),
                ('itemtime', models.DateTimeField()),
                ('ipaddress', models.CharField(max_length=255)),
                ('queryport', models.CharField(max_length=10)),
                ('game', models.ForeignKey(to='tournaments.Game')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('rnd', models.IntegerField(help_text='round?')),
                ('mtc', models.IntegerField(help_text='match?')),
                ('server', models.IntegerField()),
                ('top_x_advance', models.IntegerField(default=1)),
                ('bracket', models.CharField(max_length=3)),
                ('map', models.CharField(max_length=120)),
            ],
            options={
                'verbose_name_plural': 'matches',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MatchesScoreVote',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('entry_val', models.IntegerField()),
                ('match', models.ForeignKey(to='tournaments.Match')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MatchesTeam',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('top', models.BooleanField(default=False)),
                ('score', models.IntegerField(default=None)),
                ('match', models.ForeignKey(to='tournaments.Match')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='matchesscorevote',
            name='entry_id',
            field=models.ForeignKey(to='tournaments.MatchesTeam'),
            preserve_default=True,
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('ranking', models.IntegerField(default=0)),
                ('in_ladder', models.BooleanField(default=False)),
                ('ladder_ranking', models.IntegerField()),
                ('user', models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PollMap',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('filename', models.CharField(max_length=255)),
                ('selected', models.BooleanField(default=False)),
                ('filedesc', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('ipaddress', models.CharField(max_length=150, help_text='do not forget to put the port at the end of the address.')),
                ('queryport', models.CharField(max_length=10)),
                ('game', models.ForeignKey(to='tournaments.Game')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('sig', models.CharField(max_length=20)),
                ('sigplace', models.BooleanField(default=False)),
                ('ranking', models.IntegerField(default=0)),
                ('in_ladder', models.BooleanField(default=False)),
                ('ladder_ranking', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='player',
            name='team',
            field=models.ForeignKey(null=True, to='tournaments.Team', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='matchesteam',
            name='team',
            field=models.ForeignKey(to='tournaments.Team'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='team',
            name='captain',
            field=models.ForeignKey(to='tournaments.Player'),
            preserve_default=True,
        ),
        migrations.CreateModel(
            name='TeamType',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('onename', models.CharField(max_length=100, help_text='team one name')),
                ('onecolor', models.CharField(max_length=10, help_text='color of the team - in hex [ie: #ff0000] or in standard color name format [ie: red]')),
                ('twoname', models.CharField(max_length=100, help_text='team two name')),
                ('twocolor', models.CharField(max_length=10, help_text='color of the team - in hex [ie: #ff0000] or in standard color name format [ie: red]')),
                ('game', models.ForeignKey(to='tournaments.Game')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=255, help_text='tournament name')),
                ('itemtime', models.DateTimeField(help_text='date and time of tournament')),
                ('url_stats', models.CharField(max_length=255, help_text='url to statistics for the tournament')),
                ('random', models.BooleanField(help_text='random teams?', default=False)),
                ('per_team', models.IntegerField(help_text='maximum players per team')),
                ('max_teams', models.IntegerField(help_text='maximum number of teams (empty/0 = no max)')),
                ('ffa', models.BooleanField(help_text='free for all? (guess)', default=False)),
                ('marathon', models.BooleanField(help_text='part of the global marathon tournament?', default=False)),
                ('lockteams', models.BooleanField(help_text='lock team creation?', default=False)),
                ('lockjoin', models.BooleanField(help_text='lock team joining and quitting?', default=False)),
                ('lockstart', models.BooleanField(db_index=True, default=False)),
                ('lockfinish', models.BooleanField(default=False)),
                ('playforthird', models.BooleanField(help_text='an extra round in single elimination tournaments that determines 3rd and 4th place.', default=False)),
                ('doublefinal', models.BooleanField(help_text='for double elimination tournaments -- if the winner of the winners bracket has to lose twice to lose the tournament.', default=False)),
                ('switchover', models.IntegerField(help_text='the round number for combination tournaments to switch.', default=False)),
                ('rrsplit', models.IntegerField(help_text='how many teams are in each split of the round robin.', default=0)),
                ('timelimit', models.DateTimeField(help_text='for ladder tournaments and maybe round robin tournaments')),
                ('notes', models.BinaryField(editable=False, help_text='tournament rules/notes')),
                ('settings', models.BinaryField(editable=False)),
                ('tentative', models.BooleanField(db_index=True, help_text='classify as tentative?', default=False)),
                ('game', models.ForeignKey(help_text='the game for which this tournament is for', to='tournaments.Game')),
                ('moderator', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('teamcolors', models.ForeignKey(null=True, to='tournaments.TeamType')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='team',
            name='tourney',
            field=models.ForeignKey(to='tournaments.Tournament'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='server',
            name='tourney',
            field=models.ForeignKey(null=True, to='tournaments.Tournament', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pollmap',
            name='tourney',
            field=models.ForeignKey(null=True, to='tournaments.Tournament'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='player',
            name='tourney',
            field=models.ForeignKey(null=True, to='tournaments.Tournament'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='matchesteam',
            name='tourney',
            field=models.ForeignKey(to='tournaments.Tournament'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='matchesscorevote',
            name='tourney',
            field=models.ForeignKey(to='tournaments.Tournament'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='match',
            name='tourney',
            field=models.ForeignKey(to='tournaments.Tournament'),
            preserve_default=True,
        ),
        migrations.CreateModel(
            name='TournamentType',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('type_num', models.IntegerField()),
                ('name', models.CharField(max_length=200)),
                ('time', models.IntegerField()),
                ('minimum_teams', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='tournament',
            name='tournament_type',
            field=models.ForeignKey(to='tournaments.TournamentType'),
            preserve_default=True,
        ),
    ]
