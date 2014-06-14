# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Module'
        db.create_table('cl_module_module', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=45)),
            ('ordernum', self.gf('django.db.models.fields.IntegerField')()),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=45)),
            ('required', self.gf('django.db.models.fields.CharField')(max_length=45)),
        ))
        db.send_create_signal('cl_module', ['Module'])


    def backwards(self, orm):
        # Deleting model 'Module'
        db.delete_table('cl_module_module')


    models = {
        'cl_module.module': {
            'Meta': {'object_name': 'Module'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'ordernum': ('django.db.models.fields.IntegerField', [], {}),
            'required': ('django.db.models.fields.CharField', [], {'max_length': '45'})
        }
    }

    complete_apps = ['cl_module']