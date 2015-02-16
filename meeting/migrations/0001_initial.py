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
            name='Meeting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('person', models.CharField(max_length=30)),
                ('company', models.CharField(default=b'', max_length=30, blank=True)),
                ('date', models.DateTimeField()),
                ('location', models.CharField(default=b'', max_length=100)),
                ('priority', models.PositiveIntegerField(default=2, choices=[(3, b'Important'), (2, b'Standard'), (1, b'Casual')])),
                ('notes', models.CharField(default=b'', max_length=180)),
                ('user', models.ForeignKey(related_name='meetings', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
