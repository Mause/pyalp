# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('ordernum', models.IntegerField()),
                ('enabled', models.BooleanField(default=True)),
                ('description', models.CharField(max_length=45)),
                ('required', models.CharField(max_length=45, blank=True, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
