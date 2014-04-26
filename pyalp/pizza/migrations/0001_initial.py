# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Pizza'
        db.create_table('pizza_pizza', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pizza', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('price_currency', self.gf('djmoney.models.fields.CurrencyField')()),
            ('price', self.gf('djmoney.models.fields.MoneyField')(decimal_places=2, max_digits=20, default_currency='XYZ')),
            ('enabled', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal('pizza', ['Pizza'])

        # Adding model 'PizzaOrder'
        db.create_table('pizza_pizzaorder', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('orderer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('pizza', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pizza.Pizza'])),
            ('quantity', self.gf('django.db.models.fields.BigIntegerField')()),
            ('paid', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('delivered', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('pizza', ['PizzaOrder'])


    def backwards(self, orm):
        # Deleting model 'Pizza'
        db.delete_table('pizza_pizza')

        # Deleting model 'PizzaOrder'
        db.delete_table('pizza_pizzaorder')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'to': "orm['auth.Permission']", 'symmetrical': 'False'})
        },
        'auth.permission': {
            'Meta': {'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission', 'ordering': "('content_type__app_label', 'content_type__model', 'codename')"},
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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'user_set'", 'to': "orm['auth.Group']", 'blank': 'True', 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'user_set'", 'to': "orm['auth.Permission']", 'blank': 'True', 'symmetrical': 'False'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'", 'ordering': "('name',)"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'pizza.pizza': {
            'Meta': {'object_name': 'Pizza'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'enabled': ('django.db.models.fields.BooleanField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pizza': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'price': ('djmoney.models.fields.MoneyField', [], {'decimal_places': '2', 'max_digits': '20', 'default_currency': "'XYZ'"}),
            'price_currency': ('djmoney.models.fields.CurrencyField', [], {})
        },
        'pizza.pizzaorder': {
            'Meta': {'object_name': 'PizzaOrder'},
            'delivered': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'orderer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'paid': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'pizza': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pizza.Pizza']"}),
            'quantity': ('django.db.models.fields.BigIntegerField', [], {})
        }
    }

    complete_apps = ['pizza']