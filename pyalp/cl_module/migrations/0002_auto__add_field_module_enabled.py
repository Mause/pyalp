# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Module.enabled'
        db.add_column('cl_module_module', 'enabled',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Module.enabled'
        db.delete_column('cl_module_module', 'enabled')


    models = {
        'cl_module.module': {
            'Meta': {'object_name': 'Module'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'ordernum': ('django.db.models.fields.IntegerField', [], {}),
            'required': ('django.db.models.fields.CharField', [], {'max_length': '45'})
        }
    }

    complete_apps = ['cl_module']