# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'PollMap.tourney'
        db.add_column('tournaments_pollmap', 'tourney',
                      self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['tournaments.Tournament']),
                      keep_default=False)

        # Adding field 'PollMap.filename'
        db.add_column('tournaments_pollmap', 'filename',
                      self.gf('django.db.models.fields.CharField')(max_length=255, default=''),
                      keep_default=False)

        # Adding field 'PollMap.selected'
        db.add_column('tournaments_pollmap', 'selected',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'PollMap.filedesc'
        db.add_column('tournaments_pollmap', 'filedesc',
                      self.gf('django.db.models.fields.BinaryField')(default=b''),
                      keep_default=False)

        # Adding field 'Player.tourney'
        db.add_column('tournaments_player', 'tourney',
                      self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['tournaments.Tournament']),
                      keep_default=False)

        # Adding field 'Player.user'
        db.add_column('tournaments_player', 'user',
                      self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['auth.User']),
                      keep_default=False)

        # Adding field 'Player.team'
        db.add_column('tournaments_player', 'team',
                      self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['tournaments.Team']),
                      keep_default=False)

        # Adding field 'Player.ranking'
        db.add_column('tournaments_player', 'ranking',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Player.in_ladder'
        db.add_column('tournaments_player', 'in_ladder',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Player.ladder_ranking'
        db.add_column('tournaments_player', 'ladder_ranking',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'PollMap.tourney'
        db.delete_column('tournaments_pollmap', 'tourney_id')

        # Deleting field 'PollMap.filename'
        db.delete_column('tournaments_pollmap', 'filename')

        # Deleting field 'PollMap.selected'
        db.delete_column('tournaments_pollmap', 'selected')

        # Deleting field 'PollMap.filedesc'
        db.delete_column('tournaments_pollmap', 'filedesc')

        # Deleting field 'Player.tourney'
        db.delete_column('tournaments_player', 'tourney_id')

        # Deleting field 'Player.user'
        db.delete_column('tournaments_player', 'user_id')

        # Deleting field 'Player.team'
        db.delete_column('tournaments_player', 'team_id')

        # Deleting field 'Player.ranking'
        db.delete_column('tournaments_player', 'ranking')

        # Deleting field 'Player.in_ladder'
        db.delete_column('tournaments_player', 'in_ladder')

        # Deleting field 'Player.ladder_ranking'
        db.delete_column('tournaments_player', 'ladder_ranking')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80', 'unique': 'True'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'to': "orm['auth.Permission']", 'symmetrical': 'False'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'object_name': 'Permission', 'unique_together': "(('content_type', 'codename'),)"},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'symmetrical': 'False', 'to': "orm['auth.Group']", 'related_name': "'user_set'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'symmetrical': 'False', 'to': "orm['auth.Permission']", 'related_name': "'user_set'"}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '30', 'unique': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'db_table': "'django_content_type'", 'object_name': 'ContentType', 'unique_together': "(('app_label', 'model'),)"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'tournaments.game': {
            'Meta': {'object_name': 'Game'},
            'current_version': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'querystr2': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'short': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'thumbs_dir': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'url_maps': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'url_update': ('django.db.models.fields.CharField', [], {'max_length': '255'})
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
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_ladder': ('django.db.models.fields.BooleanField', [], {}),
            'ladder_ranking': ('django.db.models.fields.IntegerField', [], {}),
            'ranking': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['tournaments.Team']"}),
            'tourney': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['tournaments.Tournament']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['auth.User']"})
        },
        'tournaments.pollmap': {
            'Meta': {'object_name': 'PollMap'},
            'filedesc': ('django.db.models.fields.BinaryField', [], {}),
            'filename': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'selected': ('django.db.models.fields.BooleanField', [], {}),
            'tourney': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['tournaments.Tournament']"})
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
