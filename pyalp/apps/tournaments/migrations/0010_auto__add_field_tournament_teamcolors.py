# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Tournament.teamcolors'
        db.add_column('tournaments_tournament', 'teamcolors',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tournaments.TeamType'], default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Tournament.teamcolors'
        db.delete_column('tournaments_tournament', 'teamcolors_id')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'to': "orm['auth.Permission']", 'symmetrical': 'False'})
        },
        'auth.permission': {
            'Meta': {'object_name': 'Permission', 'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)"},
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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'user_set'", 'blank': 'True', 'to': "orm['auth.Group']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'user_set'", 'blank': 'True', 'to': "orm['auth.Permission']", 'symmetrical': 'False'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'object_name': 'ContentType', 'db_table': "'django_content_type'", 'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'tournaments.game': {
            'Meta': {'object_name': 'Game'},
            'current_version': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'hlsw_supported': ('django.db.models.fields.BooleanField', [], {}),
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
            'filedesc': ('django.db.models.fields.TextField', [], {}),
            'filename': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'selected': ('django.db.models.fields.BooleanField', [], {}),
            'tourney': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['tournaments.Tournament']"})
        },
        'tournaments.server': {
            'Meta': {'object_name': 'Server'},
            'game': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['tournaments.Game']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ipaddress': ('django.db.models.fields.GenericIPAddressField', [], {'max_length': '39'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'queryport': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'tourney': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['tournaments.Tournament']"})
        },
        'tournaments.team': {
            'Meta': {'object_name': 'Team'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'tournaments.teamtype': {
            'Meta': {'object_name': 'TeamType'},
            'game': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['tournaments.Game']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'onecolor': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'onename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'twocolor': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'twoname': ('django.db.models.fields.CharField', [], {'max_length': '100'})
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
            'lockstart': ('django.db.models.fields.BooleanField', [], {'db_index': 'True'}),
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
            'teamcolors': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['tournaments.TeamType']"}),
            'tentative': ('django.db.models.fields.BooleanField', [], {}),
            'timelimit': ('django.db.models.fields.DateTimeField', [], {}),
            'ttype': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['tournaments.TournamentType']"}),
            'url_stats': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'tournaments.tournamenttype': {
            'Meta': {'object_name': 'TournamentType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'minimum_teams': ('django.db.models.fields.IntegerField', [], {}),
            'time': ('django.db.models.fields.IntegerField', [], {}),
            'tournament_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'type_num': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['tournaments']