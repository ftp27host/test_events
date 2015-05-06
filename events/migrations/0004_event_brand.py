# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_event_background'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='brand',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
