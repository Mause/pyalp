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
            name='NewsItem',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('itemtime', models.DateTimeField()),
                ('headline', models.CharField(max_length=60)),
                ('news_article', models.CharField(max_length=1500)),
                ('hide_item', models.BooleanField(default=False, db_index=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL, editable=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
