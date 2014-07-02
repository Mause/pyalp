# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TechSupportRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('itemtime', models.DateTimeField()),
                ('severity', models.IntegerField()),
                ('fixed', models.BooleanField(default=False)),
                ('info', models.TextField()),
                ('result', models.TextField()),
                ('assigned_to', models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL)),
                ('fixer', models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
