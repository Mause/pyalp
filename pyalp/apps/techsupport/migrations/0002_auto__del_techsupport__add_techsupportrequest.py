# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'TechSupport'
        db.delete_table('techsupport_techsupport')

        # Adding model 'TechSupportRequest'
        db.create_table('techsupport_techsupportrequest', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='user', to=orm['auth.User'])),
            ('itemtime', self.gf('django.db.models.fields.DateTimeField')()),
            ('severity', self.gf('django.db.models.fields.IntegerField')()),
            ('fixed', self.gf('django.db.models.fields.BooleanField')()),
            ('fixer', self.gf('django.db.models.fields.related.ForeignKey')(null=True, related_name='fixer', to=orm['auth.User'])),
            ('info', self.gf('django.db.models.fields.TextField')()),
            ('result', self.gf('django.db.models.fields.TextField')()),
            ('assigned_to', self.gf('django.db.models.fields.related.ForeignKey')(null=True, related_name='assigned_to', to=orm['auth.User'])),
        ))
        db.send_create_signal('techsupport', ['TechSupportRequest'])


    def backwards(self, orm):
        # Adding model 'TechSupport'
        db.create_table('techsupport_techsupport', (
            ('itemtime', self.gf('django.db.models.fields.DateTimeField')()),
            ('assigned_to', self.gf('django.db.models.fields.related.ForeignKey')(null=True, related_name='assigned_to', to=orm['auth.User'])),
            ('result', self.gf('django.db.models.fields.TextField')()),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('info', self.gf('django.db.models.fields.TextField')()),
            ('fixer', self.gf('django.db.models.fields.related.ForeignKey')(null=True, related_name='fixer', to=orm['auth.User'])),
            ('severity', self.gf('django.db.models.fields.IntegerField')()),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='user', to=orm['auth.User'])),
            ('fixed', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal('techsupport', ['TechSupport'])

        # Deleting model 'TechSupportRequest'
        db.delete_table('techsupport_techsupportrequest')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['auth.Permission']", 'blank': 'True'})
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
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'user_set'", 'symmetrical': 'False', 'to': "orm['auth.Group']", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'user_set'", 'symmetrical': 'False', 'to': "orm['auth.Permission']", 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'db_table': "'django_content_type'", 'object_name': 'ContentType', 'unique_together': "(('app_label', 'model'),)", 'ordering': "('name',)"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'techsupport.techsupportrequest': {
            'Meta': {'object_name': 'TechSupportRequest'},
            'assigned_to': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'related_name': "'assigned_to'", 'to': "orm['auth.User']"}),
            'fixed': ('django.db.models.fields.BooleanField', [], {}),
            'fixer': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'related_name': "'fixer'", 'to': "orm['auth.User']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('django.db.models.fields.TextField', [], {}),
            'itemtime': ('django.db.models.fields.DateTimeField', [], {}),
            'result': ('django.db.models.fields.TextField', [], {}),
            'severity': ('django.db.models.fields.IntegerField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'user'", 'to': "orm['auth.User']"})
        }
    }

    complete_apps = ['techsupport']