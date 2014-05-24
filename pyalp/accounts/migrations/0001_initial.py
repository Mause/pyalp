# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'UserMetadata'
        db.create_table('accounts_usermetadata', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('paid', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('language', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('skin', self.gf('django.db.models.fields.CharField')(max_length=45)),
            ('dateformat', self.gf('django.db.models.fields.CharField')(max_length=45)),
            ('display_email', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('gaming_group', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('quote', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('room_loc', self.gf('django.db.models.fields.IntegerField')()),
            ('caffeine_mg', self.gf('django.db.models.fields.FloatField')()),
            ('proficiency', self.gf('django.db.models.fields.IntegerField')()),
            ('recent_ip', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('display_ip', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('priv_level', self.gf('django.db.models.fields.IntegerField')()),
            ('date_of_arrival', self.gf('django.db.models.fields.DateTimeField')()),
            ('date_of_departure', self.gf('django.db.models.fields.DateTimeField')()),
            ('sharename', self.gf('django.db.models.fields.CharField')(max_length=35)),
        ))
        db.send_create_signal('accounts', ['UserMetadata'])

        # Adding model 'ComputerSpecification'
        db.create_table('accounts_computerspecification', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], null=True, unique=True)),
            ('processor', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('processor_speed', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('processor_type', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('memory', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('memory_type', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('harddrive_storage', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('gpu', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('gpu_type', self.gf('django.db.models.fields.CharField')(max_length=60)),
        ))
        db.send_create_signal('accounts', ['ComputerSpecification'])


    def backwards(self, orm):
        # Deleting model 'UserMetadata'
        db.delete_table('accounts_usermetadata')

        # Deleting model 'ComputerSpecification'
        db.delete_table('accounts_computerspecification')


    models = {
        'accounts.computerspecification': {
            'Meta': {'object_name': 'ComputerSpecification'},
            'gpu': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'gpu_type': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'harddrive_storage': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'memory': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'memory_type': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'processor': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'processor_speed': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'processor_type': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'null': 'True', 'unique': 'True'})
        },
        'accounts.usermetadata': {
            'Meta': {'object_name': 'UserMetadata'},
            'caffeine_mg': ('django.db.models.fields.FloatField', [], {}),
            'date_of_arrival': ('django.db.models.fields.DateTimeField', [], {}),
            'date_of_departure': ('django.db.models.fields.DateTimeField', [], {}),
            'dateformat': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'display_email': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'display_ip': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'gaming_group': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'paid': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'priv_level': ('django.db.models.fields.IntegerField', [], {}),
            'proficiency': ('django.db.models.fields.IntegerField', [], {}),
            'quote': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'recent_ip': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'room_loc': ('django.db.models.fields.IntegerField', [], {}),
            'sharename': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'skin': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'blank': 'True', 'symmetrical': 'False'})
        },
        'auth.permission': {
            'Meta': {'unique_together': "(('content_type', 'codename'),)", 'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'object_name': 'Permission'},
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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'related_name': "'user_set'", 'blank': 'True', 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'related_name': "'user_set'", 'blank': 'True', 'symmetrical': 'False'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'db_table': "'django_content_type'", 'unique_together': "(('app_label', 'model'),)", 'ordering': "('name',)", 'object_name': 'ContentType'},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['accounts']