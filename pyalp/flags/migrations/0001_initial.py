# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Flag'
        db.create_table('flags_flag', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('enabled', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal('flags', ['Flag'])


    def backwards(self, orm):
        # Deleting model 'Flag'
        db.delete_table('flags_flag')


    models = {
        'flags.flag': {
            'Meta': {'object_name': 'Flag'},
            'enabled': ('django.db.models.fields.BooleanField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['flags']