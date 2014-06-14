# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Match'
        db.create_table('tournaments_match', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('tournaments', ['Match'])

        # Adding model 'MatchesScoreVote'
        db.create_table('tournaments_matchesscorevote', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('tournaments', ['MatchesScoreVote'])

        # Adding model 'MatchesTeam'
        db.create_table('tournaments_matchesteam', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('tournaments', ['MatchesTeam'])

        # Adding model 'Tournament'
        db.create_table('tournaments_tournament', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('ttype', self.gf('django.db.models.fields.IntegerField')()),
            ('itemtime', self.gf('django.db.models.fields.DateTimeField')()),
            ('url_stats', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('game', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tournaments.Game'])),
            ('random', self.gf('django.db.models.fields.BooleanField')()),
            ('per_team', self.gf('django.db.models.fields.IntegerField')()),
            ('max_teams', self.gf('django.db.models.fields.IntegerField')()),
            ('ffa', self.gf('django.db.models.fields.BooleanField')()),
            ('marathon', self.gf('django.db.models.fields.BooleanField')()),
            ('lockteams', self.gf('django.db.models.fields.BooleanField')()),
            ('lockjoin', self.gf('django.db.models.fields.BooleanField')()),
            ('lockstart', self.gf('django.db.models.fields.BooleanField')()),
            ('lockfinish', self.gf('django.db.models.fields.BooleanField')()),
            ('playforthird', self.gf('django.db.models.fields.BooleanField')()),
            ('doublefinal', self.gf('django.db.models.fields.BooleanField')()),
            ('switchover', self.gf('django.db.models.fields.IntegerField')()),
            ('rrsplit', self.gf('django.db.models.fields.IntegerField')()),
            ('timelimit', self.gf('django.db.models.fields.DateTimeField')()),
            ('moderator', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('notes', self.gf('django.db.models.fields.BinaryField')()),
            ('settings', self.gf('django.db.models.fields.BinaryField')()),
            ('tentative', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal('tournaments', ['Tournament'])

        # Adding model 'Team'
        db.create_table('tournaments_team', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('tournaments', ['Team'])

        # Adding model 'Player'
        db.create_table('tournaments_player', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('tournaments', ['Player'])

        # Adding model 'TeamType'
        db.create_table('tournaments_teamtype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('tournaments', ['TeamType'])

        # Adding model 'Game'
        db.create_table('tournaments_game', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('tournaments', ['Game'])

        # Adding model 'PollMap'
        db.create_table('tournaments_pollmap', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('tournaments', ['PollMap'])

        # Adding model 'Moderator'
        db.create_table('tournaments_moderator', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('tournaments', ['Moderator'])


    def backwards(self, orm):
        # Deleting model 'Match'
        db.delete_table('tournaments_match')

        # Deleting model 'MatchesScoreVote'
        db.delete_table('tournaments_matchesscorevote')

        # Deleting model 'MatchesTeam'
        db.delete_table('tournaments_matchesteam')

        # Deleting model 'Tournament'
        db.delete_table('tournaments_tournament')

        # Deleting model 'Team'
        db.delete_table('tournaments_team')

        # Deleting model 'Player'
        db.delete_table('tournaments_player')

        # Deleting model 'TeamType'
        db.delete_table('tournaments_teamtype')

        # Deleting model 'Game'
        db.delete_table('tournaments_game')

        # Deleting model 'PollMap'
        db.delete_table('tournaments_pollmap')

        # Deleting model 'Moderator'
        db.delete_table('tournaments_moderator')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'blank': 'True', 'symmetrical': 'False'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'blank': 'True', 'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'blank': 'True', 'related_name': "'user_set'", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'blank': 'True', 'related_name': "'user_set'", 'symmetrical': 'False'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'db_table': "'django_content_type'", 'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType'},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'tournaments.game': {
            'Meta': {'object_name': 'Game'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'tournaments.match': {
            'Meta': {'object_name': 'Match'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'tournaments.matchesscorevote': {
            'Meta': {'object_name': 'MatchesScoreVote'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'tournaments.matchesteam': {
            'Meta': {'object_name': 'MatchesTeam'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'tournaments.moderator': {
            'Meta': {'object_name': 'Moderator'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'tournaments.player': {
            'Meta': {'object_name': 'Player'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'tournaments.pollmap': {
            'Meta': {'object_name': 'PollMap'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'tournaments.team': {
            'Meta': {'object_name': 'Team'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'tournaments.teamtype': {
            'Meta': {'object_name': 'TeamType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'tournaments.tournament': {
            'Meta': {'object_name': 'Tournament'},
            'doublefinal': ('django.db.models.fields.BooleanField', [], {}),
            'ffa': ('django.db.models.fields.BooleanField', [], {}),
            'game': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['tournaments.Game']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'itemtime': ('django.db.models.fields.DateTimeField', [], {}),
            'lockfinish': ('django.db.models.fields.BooleanField', [], {}),
            'lockjoin': ('django.db.models.fields.BooleanField', [], {}),
            'lockstart': ('django.db.models.fields.BooleanField', [], {}),
            'lockteams': ('django.db.models.fields.BooleanField', [], {}),
            'marathon': ('django.db.models.fields.BooleanField', [], {}),
            'max_teams': ('django.db.models.fields.IntegerField', [], {}),
            'moderator': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'notes': ('django.db.models.fields.BinaryField', [], {}),
            'per_team': ('django.db.models.fields.IntegerField', [], {}),
            'playforthird': ('django.db.models.fields.BooleanField', [], {}),
            'random': ('django.db.models.fields.BooleanField', [], {}),
            'rrsplit': ('django.db.models.fields.IntegerField', [], {}),
            'settings': ('django.db.models.fields.BinaryField', [], {}),
            'switchover': ('django.db.models.fields.IntegerField', [], {}),
            'tentative': ('django.db.models.fields.BooleanField', [], {}),
            'timelimit': ('django.db.models.fields.DateTimeField', [], {}),
            'ttype': ('django.db.models.fields.IntegerField', [], {}),
            'url_stats': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['tournaments']