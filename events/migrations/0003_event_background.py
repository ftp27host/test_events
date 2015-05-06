# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_event_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='background',
            field=models.ImageField(default='', upload_to=b''),
            preserve_default=False,
        ),
    ]
