# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'NewsItem'
        db.create_table('news_newsitem', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('itemtime', self.gf('django.db.models.fields.DateTimeField')()),
            ('headline', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('news_article', self.gf('django.db.models.fields.CharField')(max_length=1500)),
            ('hide_item', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal('news', ['NewsItem'])


    def backwards(self, orm):
        # Deleting model 'NewsItem'
        db.delete_table('news_newsitem')


    models = {
        'news.newsitem': {
            'Meta': {'object_name': 'NewsItem'},
            'headline': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'hide_item': ('django.db.models.fields.BooleanField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'itemtime': ('django.db.models.fields.DateTimeField', [], {}),
            'news_article': ('django.db.models.fields.CharField', [], {'max_length': '1500'})
        }
    }

    complete_apps = ['news']