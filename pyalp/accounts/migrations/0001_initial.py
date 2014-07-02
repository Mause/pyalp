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
            name='ComputerSpecification',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('processor', models.CharField(max_length=60)),
                ('processor_speed', models.CharField(max_length=60)),
                ('processor_type', models.CharField(max_length=60, help_text='x64, x86, amd64_x86, etc')),
                ('memory', models.CharField(max_length=60)),
                ('memory_type', models.CharField(max_length=60)),
                ('harddrive_storage', models.CharField(max_length=60)),
                ('gpu', models.CharField(max_length=60)),
                ('gpu_type', models.CharField(max_length=60)),
                ('user', models.OneToOneField(null=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserMetadata',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('paid', models.BooleanField(default=False)),
                ('language', models.CharField(max_length=10)),
                ('skin', models.CharField(max_length=45)),
                ('dateformat', models.CharField(max_length=45)),
                ('display_email', models.BooleanField(default=False)),
                ('gaming_group', models.CharField(max_length=20)),
                ('quote', models.CharField(max_length=255)),
                ('room_loc', models.IntegerField()),
                ('caffeine_mg', models.FloatField()),
                ('proficiency', models.IntegerField()),
                ('recent_ip', models.CharField(max_length=15)),
                ('display_ip', models.BooleanField(default=False)),
                ('priv_level', models.IntegerField()),
                ('date_of_arrival', models.DateTimeField()),
                ('date_of_departure', models.DateTimeField()),
                ('sharename', models.CharField(max_length=35)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'user metadata',
            },
            bases=(models.Model,),
        ),
    ]
