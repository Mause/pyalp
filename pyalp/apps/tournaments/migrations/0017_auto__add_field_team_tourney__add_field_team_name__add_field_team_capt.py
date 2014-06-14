# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Team.tourney'
        db.add_column('tournaments_team', 'tourney',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tournaments.Tournament'], default=0),
                      keep_default=False)

        # Adding field 'Team.name'
        db.add_column('tournaments_team', 'name',
                      self.gf('django.db.models.fields.CharField')(max_length=100, default=''),
                      keep_default=False)

        # Adding field 'Team.captain'
        db.add_column('tournaments_team', 'captain',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tournaments.Player'], related_name='captain', default=0),
                      keep_default=False)

        # Adding field 'Team.sig'
        db.add_column('tournaments_team', 'sig',
                      self.gf('django.db.models.fields.CharField')(max_length=20, default=''),
                      keep_default=False)

        # Adding field 'Team.sigplace'
        db.add_column('tournaments_team', 'sigplace',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Team.ranking'
        db.add_column('tournaments_team', 'ranking',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Team.in_ladder'
        db.add_column('tournaments_team', 'in_ladder',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Team.ladder_ranking'
        db.add_column('tournaments_team', 'ladder_ranking',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Team.tourney'
        db.delete_column('tournaments_team', 'tourney_id')

        # Deleting field 'Team.name'
        db.delete_column('tournaments_team', 'name')

        # Deleting field 'Team.captain'
        db.delete_column('tournaments_team', 'captain_id')

        # Deleting field 'Team.sig'
        db.delete_column('tournaments_team', 'sig')

        # Deleting field 'Team.sigplace'
        db.delete_column('tournaments_team', 'sigplace')

        # Deleting field 'Team.ranking'
        db.delete_column('tournaments_team', 'ranking')

        # Deleting field 'Team.in_ladder'
        db.delete_column('tournaments_team', 'in_ladder')

        # Deleting field 'Team.ladder_ranking'
        db.delete_column('tournaments_team', 'ladder_ranking')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'to': "orm['auth.Permission']", 'symmetrical': 'False'})
        },
        'auth.permission': {
            'Meta': {'object_name': 'Permission', 'unique_together': "(('content_type', 'codename'),)", 'ordering': "('content_type__app_label', 'content_type__model', 'codename')"},
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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'to': "orm['auth.Group']", 'related_name': "'user_set'", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'to': "orm['auth.Permission']", 'related_name': "'user_set'", 'symmetrical': 'False'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'db_table': "'django_content_type'", 'object_name': 'ContentType', 'unique_together': "(('app_label', 'model'),)", 'ordering': "('name',)"},
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
            'bracket': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'map': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'mtc': ('django.db.models.fields.IntegerField', [], {}),
            'rnd': ('django.db.models.fields.IntegerField', [], {}),
            'server': ('django.db.models.fields.IntegerField', [], {}),
            'top_x_advance': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'tourney': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['tournaments.Tournament']"})
        },
        'tournaments.matchesscorevote': {
            'Meta': {'object_name': 'MatchesScoreVote'},
            'entry_id': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['tournaments.MatchesTeam']"}),
            'entry_val': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'match': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['tournaments.Match']"}),
            'tourney': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['tournaments.Tournament']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'tournaments.matchesteam': {
            'Meta': {'object_name': 'MatchesTeam'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'match': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['tournaments.Match']"}),
            'score': ('django.db.models.fields.IntegerField', [], {}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['tournaments.Team']"}),
            'top': ('django.db.models.fields.BooleanField', [], {}),
            'tourney': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['tournaments.Tournament']"})
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
            'captain': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['tournaments.Player']", 'related_name': "'captain'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_ladder': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ladder_ranking': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ranking': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sig': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'sigplace': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'tourney': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['tournaments.Tournament']"})
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
            'teamcolors': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['tournaments.TeamType']"}),
            'tentative': ('django.db.models.fields.BooleanField', [], {}),
            'timelimit': ('django.db.models.fields.DateTimeField', [], {}),
            'tournament_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['tournaments.TournamentType']"}),
            'url_stats': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'tournaments.tournamenttype': {
            'Meta': {'object_name': 'TournamentType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'minimum_teams': ('django.db.models.fields.IntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'time': ('django.db.models.fields.IntegerField', [], {}),
            'type_num': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['tournaments']